from fastapi import APIRouter, Request
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from app.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_URI

router = APIRouter()
scope = "user-top-read playlist-read-private playlist-read-collaborative"

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_CLIENT_URI,
    scope=scope,
    cache_path=None,      
    show_dialog=True 
)

@router.get("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return {"auth_url": auth_url}

@router.get("/callback") 
def callback(request: Request):
    code = request.query_params.get("code")
    if not code:
        return {"error": "No code found in request. Use /login flow."}
    
    try:
        access_token = sp_oauth.get_access_token(code, as_dict=False)

        return access_token


    except Exception as e:
        return {"error": str(e)}
    # return {"access_token": access_token}