from ships_tracker.ships.celery import app
from ships_tracker.utils.data_uploader import upload_new_data


@app.task
def nightly_upload():
    upload_new_data()
