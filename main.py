from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"response": "Home route"}


@app.get("/ping/")
async def ping():
    return {"response": "pong"}
