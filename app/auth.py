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
    scope=scope
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

        sp = Spotify(auth=access_token)
        top_tracks = sp.current_user_top_tracks(limit=5)
        
        tracks_info = [{"name": t['name'], "artist": t['artists'][0]['name']} for t in top_tracks['items']]
        
        playlists = sp.current_user_playlists(limit=5)
        playlists_info = []
        for p in playlists.get('items',[]):
            tracks_total = p.get('tracks', {}).get('total', 0)
            playlists_info.append({
                "name":p.get('name', 'Unknown'),
                "total_tracks": tracks_total
            })
            
        return {"top_tracks": tracks_info, "playlists": playlists_info}
    except Exception as e:
        return {"error": str(e)}
    # return {"access_token": access_token}