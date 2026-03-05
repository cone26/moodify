# Mood Music Recommendation 🎧

A simple backend service that recommends music based on a user's mood.

The app connects to the Spotify API to get a user's top tracks, then uses an external API to get audio features for each track. Songs are filtered using predefined mood rules.

---

## Features

- Spotify OAuth login
- Get user's top tracks from Spotify
- Fetch audio features from an external API
- Recommend songs based on mood

Example moods:

- sad
- study
- dance
- workout

---

## Tech Stack

- Python
- FastAPI
- Spotify Web API
- Spotipy
- Requests
- Uvicorn

---

## Project Structure

app
├ main.py
├ routes
│ ├ auth_router.py
│ ├ audio_router.py
│ └ recommend_router.py
├ services
│ ├ spotify_service.py
│ ├ mood_service.py
│ └ feature_service.py
└ utils
└ mood_mapping.py

---

## How it works

1. User logs in with Spotify
2. The app gets the user's top tracks
3. Audio features are fetched from an external API
4. Tracks are filtered based on mood rules
5. Recommended songs are returned

Example request:

GET /recommend?mood=dance

---

## Run the project

Create virtual environment

python -m venv venv

Install dependencies

pip install -r requirements.txt

Run the server

uvicorn app.main:app --reload

Open API docs

http://127.0.0.1:8000/docs

---

## Future improvements

- Faster API calls with async
- Playlist auto creation
- Save track data in a database
- Context-based recommendations
