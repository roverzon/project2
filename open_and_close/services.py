import pandas as pd
from polygon import RESTClient
from open_and_close.models import OpenClose


def polygon_open_and_close_api(symbol, from_, end_):
    start_date = from_
    end_date = end_
    dates = pd.bdate_range(start=start_date, end=end_date)

    with RESTClient(auth_key='u8arVdihlX_6p_pRuvRUwa94YmI4Zrny') as client:
        for date in dates:
            try:
                rep = client.stocks_equities_daily_open_close(symbol=symbol, date=date.strftime('%Y-%m-%d'))
                if rep.symbol != '':
                    openAndClose = OpenClose(
                        symbol=symbol,
                        date=date,
                        open=rep.open,
                        high=rep.high,
                        low=rep.low,
                        close=rep.close,
                        afterHours=rep.after_hours,
                        preMarket=rep.preMarket,
                        volume=rep.volume
                    )
                    text = f"Symbol:{symbol} at date {date}".format(symbol=symbol, date=date)
                    print(text)
                    openAndClose.save()
            except:
                print(f"Symbol:{symbol} has no trading data on {date}".format(symbol, date))
