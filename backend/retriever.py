import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_disaster_data():
    """Fetches real-time disaster data from multiple APIs."""
    api_endpoints = {
        "earthquakes": os.getenv("USGS_API_URL"),
        "natural_events": os.getenv("NASA_EONET_API_URL"),
        "alerts": os.getenv("GDACS_API_URL"),
        "weather": os.getenv("OPEN_METEO_API_URL"),
    }

    disaster_data = {}

    for event_type, url in api_endpoints.items():
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code == 200:
                disaster_data[event_type] = response.json()
            else:
                disaster_data[event_type] = {"error": f"Failed to fetch data: {response.status_code}"}
        except Exception as e:
            disaster_data[event_type] = {"error": str(e)}

    return disaster_data
