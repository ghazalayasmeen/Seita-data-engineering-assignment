from fastapi import FastAPI, HTTPException
from seita_api.utils import get_forecast, get_tomorrow
from configs import port, host
import os

# Set the working directory to the root of your project
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI()


@app.get("/forecasts")
async def forecasts(now: str, then: str):
    """
    Endpoint to get the three most recent weather forecasts between the specified time range.

    Parameters:
        - now (str): A string representing the current datetime in ISO format.
        - then (str): A string representing the end datetime in ISO format.

    Returns:
        dict: A dictionary containing the "forecasts" key with a list of the three most recent forecasts.

    Raises:
        HTTPException: If an error occurs during the processing of the request.
    """
    try:
        result = get_forecast(now, then)
        return {"forecasts": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/tomorrow")
async def tomorrow(now: str):
    """
    Endpoint to check if the next day is expected to be warm, sunny, and windy based on the weather dataset.

    Parameters:
        - now (str): A string representing the current datetime in ISO format.

    Returns:
        dict: A dictionary containing the boolean values for "is_warm", "is_sunny", and "is_windy".

    Raises:
        HTTPException: If an error occurs during the processing of the request.
    """
    try:
        result = get_tomorrow(now)
        return {
            "is_warm": result[0],
            "is_sunny": result[1],
            "is_windy": result[2]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=host, port=int(port))
