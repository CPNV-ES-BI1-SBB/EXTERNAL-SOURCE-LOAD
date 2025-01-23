import pytest
from pytest_bdd import scenarios, given, when, then
from unittest.mock import patch
from app.routes.jobs import process
from app.schemas.requests import JobRequest

scenarios("jobs.feature")  # Lien vers le .feature


@pytest.fixture
def test_context():
    """
    Prepare the context (Given/When/Then).
    """
    return {
        "job_id": "",
        "data_source": "",
        "result": "",  # To store the return of the process function
    }


# ---------------------------------------------------------
# GIVEN
# ---------------------------------------------------------
@given('A job_id "123"')
def given_job_id_123(test_context):
    test_context["job_id"] = "123"


@given('A dataSource "http://fake.url/data.json"')
def given_data_source(test_context):
    test_context["data_source"] = "http://fake.url/data.json"


# ---------------------------------------------------------
# WHEN
# ---------------------------------------------------------
@when('The client call the route with the job_id and the dataSource')
def when_call_process(test_context):
    """
    Direct call of the process(...) function
    by mocking external services (fetchRequest, insert_data, etc.).
    """
    fake_raw_data = {
        "name": "Yverdon-les-Bains",
        "departures": [
            {
                "departureStationName": "Yverdon-les-Bains",
                "destinationStationName": "Lausanne",
                "departureTime": "2024-12-09T08:00:00",
                "train": {"g": "IC", "l": "5"},
                "platform": "2",
                "sector": "D"
            }
        ]
    }

    with patch("app.services.http_request_fetcher.HttpRequestFetcher.fetchRequest") as mock_fetch, \
            patch("app.services.json_serializer.JsonSerializer.serialize") as mock_serialize, \
            patch("app.providers.amazon_rds_provider.RdsClient.insert_data") as mock_insert:
        # We define the behavior of mocks
        mock_fetch.return_value = fake_raw_data
        mock_serialize.return_value = '{"some":"serialized_data"}'
        mock_insert.return_value = None

        # We create a request_body as your function expects
        job_request = JobRequest(dataSource=test_context["data_source"])

        # Call process(...) directly without using FastAPI
        result = process(job_request)
        test_context["result"] = result


# ---------------------------------------------------------
# THEN
# ---------------------------------------------------------
@then('The service return a HTTP code 200 and a success message')
def then_success_response(test_context):
    result = test_context["result"]
    assert result["status"] == "success"
    assert result["message"] == "Data processed and inserted successfully."
