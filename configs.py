import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Path to the weather data CSV file
PATH_TO_DATA = os.getenv("PATH_TO_DATA")

# Test datetime values for simulation
now_datetime = os.getenv("TEST_NOW")
then_datetime = os.getenv("TEST_THEN")

# Server configurations
port = os.getenv("PORT")
host = os.getenv("HOST_ADDRESS")

# Thresholds for weather conditions
warm_threshold = os.getenv("WARM_THRESHOLD")
sunny_threshold = os.getenv("SUNNY_THRESHOLD")
windy_threshold = os.getenv("WIND_THRESHOLD")

