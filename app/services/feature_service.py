from app.utils.mood_mapping import MOOD_AUDIO_FEATURE_MAP
import requests
import os
from dotenv import load_dotenv

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

def get_audio_features(track_id):

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY
    }

    params = {
        "track_id": track_id
    }
    url = "https://track-analysis.p.rapidapi.com/pktx/analysis"
    response = requests.get(url, headers=headers, params=params)
    print(response.status_code)
    if response.status_code != 200:
        return None

    return response.json()

def enrich_tracks_with_features(tracks):
    tracks_with_features = []
    for track in tracks:
        features = get_audio_features(track["id"])

        print(features)
        if not features:
            continue
        
        tracks_with_features.append({
            **track,
            "features": {
                "valence": features.get("valence"),
                "energy": features.get("energy"),
                "danceability": features.get("danceability"),
                "acousticness": features.get("acousticness"),
                "tempo": features.get("tempo")
            }
        })

    return tracks_with_features