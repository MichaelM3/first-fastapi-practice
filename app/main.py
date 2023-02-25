from fastapi import FastAPI
from config import engine
from models import User

User.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return { "message": "Hello World!" }
