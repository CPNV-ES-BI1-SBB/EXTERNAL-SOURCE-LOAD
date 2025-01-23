from fastapi import APIRouter
from app.utils.config import DATABASE_URL
from app.schemas.requests import JobRequest
from app.services.http_request_fetcher import fetchRequest
from app.services.json_serializer import serialize
from app.providers.amazon_rds_provider import amazonRDSCon
from app.providers.sql_builder import insert_object

router = APIRouter()
connection_string = DATABASE_URL


@router.post("/{job_id}")
def process(request: JobRequest):
    """
    # Description
    This route accepts a URL to retrieve the data and process the loading of the data into the Cloud provider.
    """
    try:
        raw_data = fetchRequest(request.dataSource)

        data = serialize(raw_data)

        with amazonRDSCon() as provider:
            try:
                for obj in data:
                    insert_object(provider, obj)
                    provider.commit()
            except Exception as e:
                provider.rollback()
                return {"status": "error", "message": str(e)}

        return {"status": "success", "message": "Data processed and inserted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
