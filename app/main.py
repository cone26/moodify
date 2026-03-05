from fastapi import FastAPI
from app.routes import (
    audio, recommend_router, auth_router
    )

app = FastAPI(title="Moddify - Context-aware Music Recommender")
app.include_router(auth_router.router, prefix="/auth")
app.include_router(audio.router)
app.include_router(recommend_router.router)

@app.get("/")
def root():
    return {"message": "Hello Moodify!"}


# if __name__ == "__main__":
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)