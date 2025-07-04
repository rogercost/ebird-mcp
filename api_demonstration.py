import os
from dotenv import load_dotenv

from ebird.api import get_nearby_observations

load_dotenv()

api_key = os.environ['EBIRD_API_KEY']

# LGA Airport coordinates
lat = 40.7747
lon = -73.8719

records = get_nearby_observations(api_key, lat, lon, dist=50)

print(records)