from dotenv import load_dotenv
import os

load_dotenv()


def get_config():
    """Fetch database configurations from environment variables."""
    return {
        "redshift": {
            "dbname": os.getenv("REDSHIFT_DBNAME"),
            "user": os.getenv("REDSHIFT_USER"),
            "password": os.getenv("REDSHIFT_PASSWORD"),
            "host": os.getenv("REDSHIFT_HOST"),
            "port": os.getenv("REDSHIFT_PORT"),
        },
        "synapse": {
            "driver": os.getenv("SYNAPSE_DRIVER"),
            "server": os.getenv("SYNAPSE_SERVER"),
            "database": os.getenv("SYNAPSE_DATABASE"),
            "uid": os.getenv("SYNAPSE_UID"),
            "pwd": os.getenv("SYNAPSE_PWD"),
        },
        "snowflake": {
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
            "database": os.getenv("SNOWFLAKE_DATABASE"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA"),
        },
        "bigquery": {
            "project": os.getenv("BIGQUERY_PROJECT"),
            "keyfile": os.getenv("BIGQUERY_KEYFILE"),
            "dataset": os.getenv("BIGQUERY_DATASET"),
            "table": os.getenv("BIGQUERY_TABLE"),
        },

    }
