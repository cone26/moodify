from fastapi import APIRouter
from app.services.mood_service import get_track_mood

router = APIRouter()

@router.get("/audio-features")
def audio_features(track: str, artist: str):
    features = get_track_mood(track, artist)

    return {
        "track": track,
        "artist": artist,
        "features": features
    }