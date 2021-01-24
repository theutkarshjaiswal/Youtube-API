from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from scheduler import youtubeApi


def start():
    scheduler = BackgroundScheduler()
    # Here scheduler run with an interval of 10 Second
    scheduler.add_job(youtubeApi.fetch, 'interval', seconds=20)
    scheduler.start()
