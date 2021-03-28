from djangoProject.celery import app
from stock_tas.services import cross_star_api


@app.task
def cross_star_scanning_async(symbol, from_, end_):
    cross_star_api(symbol=symbol, from_=from_, end_=end_)


@app.task(name='print_msg_main')
def print_msg_main():
    print("hello world")
