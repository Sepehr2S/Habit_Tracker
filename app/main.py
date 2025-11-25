from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def test():
    return {"message": "your api is working"}