import logging


class CronJob:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("CronJob called")
    
    
    def start(self):
        self.logger.info("Cronjob Started!!!")