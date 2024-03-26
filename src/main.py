from fastapi import FastAPI
from fastapi_utilities import repeat_every
from src.cronjob.cronjob import CronJob

app = FastAPI()

cronJob = CronJob()
@app.on_event('startup')
@repeat_every(seconds=5)
def cronjob():
    cronJob.start()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/get/name")
async def get_name(name: str):
    return {"name": name}