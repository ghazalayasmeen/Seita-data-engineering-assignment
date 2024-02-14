# Seita Data Engineering Assignment

## Instructions:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the FastAPI application: `uvicorn seita_api.main:app --reload`.
4. Access the API endpoints:
   - `/forecasts`: `http://localhost:8000/forecasts?now=2024-02-13T12:00:00&then=2024-02-14T12:00:00`
   - `/tomorrow`: `http://localhost:8000/tomorrow?now=2024-02-13T12:00:00`

## Project Structure:

- `data/`: Contains the weather_forecasts.csv dataset.
- `tests/`: Holds unit tests for the endpoints.
- `seita_api/`: Contains the main application code.
- `.gitignore`: Ignores unnecessary files from version control.
- `requirements.txt`: Lists project dependencies.
- `Dockerfile`: Defines the Docker image for the FastAPI application.

## Running with Docker:

To run the application using Docker:

1. Build the Docker image: `docker build -t seita-api .`
2. Run the Docker container: `docker run -p 8000:8000 seita-api`

Make sure to adjust the port numbers as needed.

## Testing:

Run unit tests from the root directory:

```bash
python -m pytest tests/
```
# Application Logic and Workflow:
## seita_api/main.py:

    The main FastAPI application file.
    Defines two endpoints: /forecasts and /tomorrow.
    Utilizes functions from seita_api/utils.py for the endpoint logic.
    Exception handling is in place to handle errors gracefully and return appropriate HTTP status codes.

## seita_api/utils.py:
get_forecast(now, then):

    Reads weather data from the CSV file specified in configs.py.
    Filters data based on the given time range and belief horizon.
    Sorts the data to get the three most recent forecasts for the specified time.

get_tomorrow(now):

    Reads weather data from the CSV file specified in configs.py.
    Filters data for the next day.
    Separates sensor data for temperature, irradiance, and wind speed.
    Determines if the thresholds for being warm, sunny, and windy are breached.

## configs.py:

    Centralizes configuration variables like file paths, datetime values, server configurations, and weather thresholds.
    Loads environment variables from a .env file using the python-dotenv library.

## tests/test_endpoints.py:

    Contains unit tests for the FastAPI endpoints.
    Uses the fastapi.testclient to simulate API requests and checks the responses.
