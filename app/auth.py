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

        sp = Spotify(auth=access_token)
        top_tracks_data = sp.current_user_top_tracks(limit=5)
        
        top_tracks_info = []
        track_ids = []

        for t in top_tracks_data['items']:
            track_ids.append(t['id'])
            top_tracks_info.append({
                "id":t['id'],
                "name": t['name'],
                "artist": t['artists'][0]['name']
            })
      
        if track_ids:
            audio_features = sp.audio_features(track_ids)
        else:   
            audio_features = []
        print('test')
        for i,features in enumerate(audio_features):
            top_tracks_info[i]['audio_features'] = features

        return {"top_tracks": top_tracks_info}


    except Exception as e:
        return {"error": str(e)}
    # return {"access_token": access_token}