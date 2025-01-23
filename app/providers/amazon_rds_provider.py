import psycopg2
from contextlib import contextmanager

from psycopg2.extras import RealDictCursor

from app.utils import config
from app.errors.custom_errors import DataBaseError


@contextmanager
def amazonRDSCon():

    conn = psycopg2.connect(config.DATABASE_URL, cursor_factory=RealDictCursor)
    if conn is None:
        raise DataBaseError("Could not connect to the database")
    try:
        yield conn
    finally:
        conn.close()
