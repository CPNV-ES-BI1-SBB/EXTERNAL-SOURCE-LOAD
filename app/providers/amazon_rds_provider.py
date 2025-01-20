import psycopg2
from .cloud_provider import IDatabaseClient
from app.models.station import Station
from app.providers.sql_builder import build_sql_statements_for_station


class RdsClient(IDatabaseClient):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def insert_data(station: "Station", connection_string: str):
        """
        Insert a station, its departures, and associated trains into the database.
        """

        statements = build_sql_statements_for_station(station)

        conn = psycopg2.connect(connection_string)
        cur = conn.cursor()

        try:
            for query, params in statements:
                cur.execute(query, params)

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

