import os
from app.errors.custom_errors import EnvironmentVariablesError
from dotenv import load_dotenv

load_dotenv()

RDS_HOST = os.getenv("RDS_HOST")
RDS_PORT = os.getenv("RDS_PORT")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DBNAME = os.getenv("RDS_DBNAME")

missing_vars = []
for var in ["RDS_HOST", "RDS_PORT", "RDS_USER", "RDS_PASSWORD", "RDS_DBNAME"]:
    if not os.getenv(var):
        missing_vars.append(var)

if missing_vars:
    raise EnvironmentVariablesError(f"Les variables d'environnement suivantes sont manquantes : {', '.join(missing_vars)}")

DATABASE_URL = f"postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DBNAME}"
