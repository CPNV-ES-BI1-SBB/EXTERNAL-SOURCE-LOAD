import app.utils.config

from app.providers.snowflake_provider import SnowflakeConnection
from bigquery_provider import BigQueryConnection
from redshift_provider import RedshiftConnection
from azure_synapse_provider import SynapseConnection

CONFIG = app.utils.config.get_config()


class DataWarehouseFactory:
    @staticmethod
    def create_connection(datawarehouse_type):
        # Select the corresponding config dictionary for this datawarehouse_type
        if datawarehouse_type not in CONFIG:
            raise ValueError(f"Unknown data warehouse type: {datawarehouse_type}")

        dw_config = CONFIG[datawarehouse_type]

        if datawarehouse_type == "snowflake":
            return SnowflakeConnection(dw_config)
        elif datawarehouse_type == "bigquery":
            return BigQueryConnection(dw_config)
        elif datawarehouse_type == "redshift":
            return RedshiftConnection(dw_config)
        elif datawarehouse_type == "synapse":
            return SynapseConnection(dw_config)
