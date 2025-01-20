from fastapi import APIRouter, HTTPException
from app.controllers.LoadingController import LoadingController

router = APIRouter()


@router.post("/process/{url}", response_model=None)
def process():
    """
    # Description
    This routes accept an url to retrieve the data and process the loading of the data into the Cloud provider.
    """

    try:
        LoadingController.process()

        # This is the response you should return
        # Replace the url with the actual download url of your service
        loaded_data_url = f"MS_NAME/process/{url}/load"

        return {"url": loaded_data_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

