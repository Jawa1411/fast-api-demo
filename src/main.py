from fastapi import FastAPI
from fastapi_utilities import repeat_every
from src.cronjob.cronjob import CronJob
import os
from typing_extensions import Required

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
    # env = getenv("Name")
    return {"name": name, "env_name": env}


def getenv(key, requires=True):
    value = os.environ.get(key)
    if value is None and Required:
        raise RuntimeError(f"Missing required config: %{key}")
    return value