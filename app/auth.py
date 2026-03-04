from fastapi import APIRouter, Request
from spotipy.oauth2 import SpotifyOAuth
from app.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_CLIENT_URI

router = APIRouter()
scope = "playlist-modify-public playlist-modify-private user-top-read"

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_CLIENT_URI,
    scope=scope
)

@router.get("/login")
def login():
    auth_url = sp_oauth.get_authorize_url()
    return {"auth_url": auth_url}

@router.get("/callback")
def callback(request: Request):
    code = request.query_params.get("code")
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']
    return {"access_token": access_token}