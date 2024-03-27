import logging
from src.database import getenv

class CronJob:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("CronJob called")
    
    
    def start(self):
        name = getenv("NAME")
        self.logger.info(f"Cronjob Started!!! {name}")