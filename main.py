from fastapi import FastAPI, HTTPException
import app.providers.db_factory as db_factory
import app.helpers.json_to_object as json_to_object
import app.helpers.object_to_sql as object_to_sql

app = FastAPI()


@app.post("/load")
async def load(data: dict):

    try:
        # Convert JSON string to Python object
        obj = json_to_object.json_to_object(data["json_data"])
        # Convert Python object to SQL queries
        sql = object_to_sql.object_to_sql(obj)
        # Open the database connection
        db = db_factory.create(data["db_type"], data["db_params"])
        # Execute the SQL queries
        db.execute(sql)

        return {"status": "success"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
