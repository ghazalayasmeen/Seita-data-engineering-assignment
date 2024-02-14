from datetime import datetime, timedelta, timezone
import pandas as pd
from configs import PATH_TO_DATA, warm_threshold, windy_threshold, sunny_threshold


def get_forecast(now, then):
    """
    Get the three most recent weather forecasts between the specified time range.

    Parameters:
        - now (str): A string representing the current datetime in ISO format.
        - then (str): A string representing the end datetime in ISO format.

    Returns:
        list: A list of dictionaries containing the three most recent forecasts.
    """
    weather_data = pd.read_csv(PATH_TO_DATA)
    weather_data["event_start"] = pd.to_datetime(weather_data["event_start"])

    # Convert strings to datetime objects and make them offset-aware
    now = datetime.fromisoformat(now).replace(tzinfo=timezone.utc)
    then = datetime.fromisoformat(then).replace(tzinfo=timezone.utc)

    # Filter data based on belief_horizon_in_sec and time range
    relevant_data = weather_data[
        (pd.to_datetime(weather_data['event_start']) >= now - weather_data['belief_horizon_in_sec'].apply(
            lambda x: timedelta(seconds=x))) &
        (pd.to_datetime(weather_data['event_start']) <= then)
        ]

    # Sort by event_start in descending order
    sorted_data = relevant_data.sort_values(by='event_start', key=pd.to_datetime, ascending=False)

    # Extract the three most recent forecasts
    recent_forecasts = sorted_data.head(3).to_dict('records')

    return recent_forecasts


def get_tomorrow(now):
    """
    Check if the next day is expected to be warm, sunny, and windy based on the weather dataset.

    Parameters:
        - now (str): A string representing the current datetime in ISO format.

    Returns:
        tuple: A tuple of three booleans indicating if the next day is expected to be warm, sunny, and windy.
    """
    weather_data = pd.read_csv(PATH_TO_DATA)
    weather_data["event_start"] = pd.to_datetime(weather_data["event_start"])

    # Convert the "now" parameter to a datetime object and make it offset-aware
    now = datetime.fromisoformat(now).replace(tzinfo=timezone.utc)

    # Filter data for the next day
    tomorrow_data = weather_data[
        (pd.to_datetime(weather_data['event_start']).dt.date == (now + timedelta(days=1)).date())
    ]

    # Separate the sensor data
    temperature = tomorrow_data.loc[tomorrow_data["sensor"].str.contains("temperature")]
    irradiance = tomorrow_data.loc[tomorrow_data["sensor"].str.contains("irradiance")]
    wind_speed = tomorrow_data.loc[tomorrow_data["sensor"].str.contains("wind_speed")]

    # Check if the thresholds are breached at least once for each type of data
    is_warm = any(temperature['event_value'].apply(lambda x: x >= int(warm_threshold)))
    is_sunny = any(irradiance['event_value'].apply(lambda x: x >= int(sunny_threshold)))
    is_windy = any(wind_speed['event_value'].apply(lambda x: x >= int(windy_threshold)))

    return is_warm, is_sunny, is_windy
