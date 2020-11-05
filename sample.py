#
#import quandl
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

#from pandas_datareader import data as web
from pandas_datareader import data as pdr
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

app.layout = html.Div(children=[
    html.H1(children='Stonks Monitor'),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Nio', 'value': 'NIO'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph'),
    html.Div(children='''
        Time Span
    '''),
    dcc.RadioItems(
        options=[
            {'label': 'Day', 'value': 'day'},
            {'label': 'Week', 'value': 'week'},
            {'label': 'Month', 'value': 'month'}
        ],
        value='day',
        labelStyle={'display': 'inline-block'},
        style={'padding':'300'}
    )
], style={'width': '200'}
)

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = pdr.get_data_yahoo(selected_dropdown_value, start=span_7_days, end=today)


    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }],
        'layout': {'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app.run_server(debug=False)