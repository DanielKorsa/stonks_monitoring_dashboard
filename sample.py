#
import quandl
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from pandas_datareader import data as web
import datetime as dt
import yfinance as yf
yf.pdr_override()#!

today = dt.datetime.now()
week = today - dt.timedelta(days=7)
span_7_days = week.replace(hour=0, minute=0, second=0, microsecond=0)
month = today - dt.timedelta(days=30)
span_30_days = month.replace(hour=0, minute=0, second=0, microsecond=0)
year = today - dt.timedelta(days=365)
span_365_days = year.replace(hour=0, minute=0, second=0, microsecond=0)

quandl_api_key = 'ngoDsHD9gkKUzPdtWkax' #! add to .ini file
#quandl.ApiConfig.api_key = api_key

app = dash.Dash('Stonks Dashboard')

app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
], style={'width': '500'})

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        name=selected_dropdown_value,
        data_source = 'quandl',
        start=dt.datetime(2017, 1, 1),
        end=today,
        #session=session,
        api_key=quandl_api_key
    )

    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server()