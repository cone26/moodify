from fastapi import FastAPI
from app.auth import router as auth_router

app = FastAPI(title="Moddify - Context-aware Musci Recommender")
app.include_router(auth_router, prefix="/auth")

@app.get("/")
def root():
    return {"message": "Hello Moodify!"}

# if __name__ == "__main__":
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)