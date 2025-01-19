import os
from dotenv import load_dotenv

load_dotenv()

RDS_HOST = os.getenv("RDS_HOST")
RDS_PORT = os.getenv("RDS_PORT")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DBNAME = os.getenv("RDS_DBNAME")


DATABASE_URL = f"postgresql://{RDS_USER}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DBNAME}"

# Raise an error if one of the RDS environment variables is not defined
if not all([RDS_HOST, RDS_PORT, RDS_USER, RDS_PASSWORD, RDS_DBNAME]):
    raise ValueError("Les variables d'environnement RDS ne sont pas toutes définies !")
