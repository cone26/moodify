from fastapi import APIRouter
from spotipy import Spotify

from app.services.spotify_service import get_top_tracks
from app.services.feature_service import (
    enrich_tracks_with_features, filter_tracks_by_mood 
)

router = APIRouter()

@router.get("/recommend")
def recommend(mood: str):
    sp = Spotify(auth="access_token")

    # user top tracks
    tracks = get_top_tracks(sp)
    # get audio features
    tracks_with_features = await enrich_tracks_with_features(tracks)
    # filter by mood
    recommended = filter_tracks_by_mood(tracks_with_features, mood)

    return {
        "mood": mood,
        "tracks": recommended
    }
