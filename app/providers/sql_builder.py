from app.models.station import Station


def build_sql_statements_for_station(station: "Station"):
    """
    Construct a list of (SQL query, tuple of parameters)
    to insert a station, its departures, and associated trains.
    """
    sql_statements = []

    insert_station_sql = """
        INSERT INTO stations (name) VALUES (%s)
    """
    sql_statements.append((insert_station_sql, (station.name,)))

    for dep in station.departures:
        insert_departure_sql = """
            INSERT INTO departures (station_name, departure_station_name, destination_station_name,
            departure_time, platform, sector)
             VALUES (%s, %s, %s, %s, %s, %s)
        """
        sql_statements.append((insert_departure_sql, (
            station.name, dep.departureStationName, dep.destinationStationName, dep.departureTime, dep.platform,
            dep.sector)))

        insert_train_sql = """
            INSERT INTO trains (type, number) VALUES (%s, %s)
        """
        sql_statements.append((insert_train_sql, (dep.train.type, dep.train.number)))

    return sql_statements
