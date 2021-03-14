from djangoProject.celery import app

@app.task
def check_all_ticker_list():
    return
