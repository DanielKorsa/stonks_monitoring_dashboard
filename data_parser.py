from pandas_datareader import data as web
import pandas as pd
#from datetime import datetime as dt
import datetime as dt
import pprint



# today = dt.datetime.now()
# week = today - dt.timedelta(days=7)
# span_7_days = week.replace(hour=0, minute=0, second=0, microsecond=0)
# month = today - dt.timedelta(days=30)
# span_30_days = month.replace(hour=0, minute=0, second=0, microsecond=0)
# year = today - dt.timedelta(days=365)
# span_365_days = year.replace(hour=0, minute=0, second=0, microsecond=0)





import yfinance as yf

company = 'NIO'

def get_ticker_ref(ticker_name):
    '''
    '''

    return yf.Ticker(ticker_name)

def get_ticker_info(ticker_ref):
    '''
    '''
    return ticker_ref.info

stonk_ref = get_ticker_ref(company)
stonk_info = get_ticker_info(stonk_ref)

stonk_data = stonk_ref.history(interval='5d')
#pprint.pprint(stonk_data)
pprint.pprint(stonk_info)


def calc_win(buy_in, current_price, shares_n):
    '''
    '''
    return (current_price - buy_in) * shares_n


alibaba = calc_win(240, 2500, 50)
print(alibaba)

nio = calc_win(21.57, 33.30, 30)
print(nio)