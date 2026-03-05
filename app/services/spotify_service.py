from spotipy import Spotify

def get_user_top_tracks(sp: Spotify, limit=10):
    data = sp.current_user_top_tracks(limit=limit)

    tracks = []

    for t in data['items']:
        tracks.append({
            "id": t["id"],
            "name": t["name"],
            "artist": t["artists"][0]["name"]
        })

    return tracks



    
    