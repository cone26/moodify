from app.utils.mood_mapping import MOOD_AUDIO_FEATURE_MAP
import requests
import os
from dotenv import load_dotenv
import httpx
import asyncio

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

def match_mood(track_features, mood):
    mapping = MOOD_AUDIO_FEATURE_MAP.get(mood)

    if not mapping:
        return False
    
    for feature, (min_v, max_v) in mapping.items():
        value = track_features.get(feature)

        if value is None:
            return False
        if not (min_v <= value <= max_v):
            return False
    
    return True

def filter_tracks_by_mood(tracks_with_features, mood):
    filtered_tracks = []
    for track in tracks_with_features:
        if match_mood(track["features"], mood):
            filtered_tracks.append(track)
    
    return filtered_tracks

async def get_audio_features(track_id):

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }

    params = {
        "track_id": track_id
    }

    try:
        url = "https://track-analysis.p.rapidapi.com/pktx/analysis"
        response = await client.get(url, headers=headers, params=params)
        if response.status_code != 200:
            return None

        features = response.json()

        return {
            **track,
            "features": {
                "valence": features.get("valence"),
                "energy": features.get("energy"),
                "danceability": features.get("danceability"),
                "acousticness": features.get("acousticness"),
                "tempo": features.get("tempo")
            }
        }
    except Exception:
        return None
    

async def enrich_tracks_with_features(tracks):
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [
            get_audio_features(client, track)
            for track in tracks
        ]

        result = await asyncio.gather(*tasks)

    return [r for r in results if r]