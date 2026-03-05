import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

def get_track_mood(track_name: str, artist_name:str):
    url = "https://track-analysis.p.rapidapi.com/pktx/analysis"

    querystring = {
        "track": track_name,
        "artist": artist_name
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code != 200:
        return None
    
    return response.json()

# {
#   "track": "The Masterplan",
#   "artist": "Oasis",
#   "features": {
#     "id": "7b1c9cc30acf2deebfa636cf7afb3e11",
#     "key": "A",
#     "mode": "major",
#     "camelot": "11B",
#     "tempo": 153,
#     "duration": "4:18",
#     "popularity": 53,
#     "energy": 95,
#     "danceability": 12,
#     "happiness": 20,
#     "acousticness": 0,
#     "instrumentalness": 80,
#     "liveness": 46,
#     "speechiness": 8,
#     "loudness": "-3 dB"
#   }
# }
