import logging
from fastapi import FastAPI
from fastapi_utilities import repeat_every
from src.cronjob.cronjob import CronJob
from src.database import getenv

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

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
    logger.info("Before getting env")
    env_name = getenv("NAME")
    logger.info(f"After getting env: {env_name}")
    return {"name": name, "env_name":env_name}
