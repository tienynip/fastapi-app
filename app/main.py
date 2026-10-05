from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "CI-CD Pineline Working--------------------Extra line added to check Tien qua dep trai-----------"}