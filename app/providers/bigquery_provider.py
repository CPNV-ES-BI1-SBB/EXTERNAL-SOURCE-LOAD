from google.cloud import bigquery
import base_db_provider


class BigQueryConnection(base_db_provider):
    def __init__(self, project_id, credentials_path):
        self.project_id = project_id
        self.credentials_path = credentials_path

    def connect(self):
        # Pour BigQuery, le client se connecte automatiquement à partir des credentials
        client = bigquery.Client.from_service_account_json(self.credentials_path, project=self.project_id)
        return client
