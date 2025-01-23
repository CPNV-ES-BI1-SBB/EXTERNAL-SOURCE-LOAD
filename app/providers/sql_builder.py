from app.providers.amazon_rds_provider import amazonRDSCon
from pydantic import BaseModel
from typing import Optional
import datetime
from app.models.station import Station
from app.models.departure import Departure
from app.models.train import Train
from app.errors.custom_errors import DataBaseError, ValidationError


def count_trains(obj: BaseModel) -> int:
    """
    Compte le nombre total de trains dans l'objet Pydantic.
    """
    count = 0
    if isinstance(obj, Station):
        for dep in obj.departures:
            count += count_trains(dep)
    elif isinstance(obj, Departure):
        if obj.train:
            count += 1
    return count


def insert_station(conn: amazonRDSCon(), station: Station) -> int:
    cursor = conn.cursor()
    print(station)
    sql = "INSERT INTO stations (name, long, lat) VALUES (%s, %s, %s) RETURNING id"
    print({"name": station.name, "long": station.long, "lat": station.lat})
    cursor.execute(sql, (station.name, station.long, station.lat))
    station_id = cursor.fetchone()["id"]
    return station_id


def insert_departure(conn: amazonRDSCon(), dep: Departure, station_id: int) -> int:
    cursor = conn.cursor()
    # Convertir departureTime en datetime
    departure_time_dt = datetime.datetime.fromtimestamp(dep.departureTime)

    sql = """
    INSERT INTO departures (
        station_id,
        destination_station_name,
        via_station_names,
        departure_time,
        platform,
        sector
    )
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    """

    cursor.execute(sql, (
        station_id,
        dep.destinationStationName,
        dep.viaStationNames,
        departure_time_dt,
        dep.platform,
        dep.sector
    ))

    departure_id = cursor.fetchone()["id"]

    return departure_id


def insert_train(conn: amazonRDSCon(), train: Train, departure_id: int) -> Optional[int]:

    cursor = conn.cursor()
    sql = "INSERT INTO trains (departure_id, type, line) VALUES (%s, %s, %s) RETURNING id"

    print({"departure_id": departure_id, "type": train.type, "line": train.line})

    cursor.execute(sql, (departure_id, train.type, train.line))
    train_id = cursor.fetchone()["id"]
    return train_id


def insert_object(conn: amazonRDSCon(), obj: BaseModel, parent_id: Optional[int] = None) -> Optional[int]:

    try:
        if isinstance(obj, Station):
            station_id = insert_station(conn, obj)
            print(f"Inserted Station : {obj.name} : {station_id}")

            for dep in obj.departures:
                departure_id = insert_departure(conn, dep, station_id)
                print(f"Inserted Departure for : {obj.name}, with id :{departure_id}, for station :{station_id}")
                if dep.train:
                    print(dep.train)
                    insert_train(conn, dep.train, departure_id)
                    print(f"Inserted Train: {obj.name}, with id :{departure_id}, for station :{station_id}")
            return station_id

        elif isinstance(obj, Departure):
            if parent_id is None:
                raise DataBaseError("Impossible d'insérer un Departure sans station_id.")

            departure_id = insert_departure(conn, obj, parent_id)

            return departure_id

        elif isinstance(obj, Train):
            if parent_id is None:
                raise DataBaseError("Impossible d'insérer un Train sans departure_id.")

            train_id = insert_train(conn, obj, parent_id)

            return train_id

        else:
            raise ValidationError(f"Type de modèle non géré : {obj.__class__.__name__}")

    except Exception as e:
        print(f"Error during insert: {e}")
        conn.rollback()
        raise e
