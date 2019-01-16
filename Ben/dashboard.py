import dash
import pandas as pd
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from pandas_datareader import data as web
from datetime import datetime as dt

from flask import Flask, render_template
app = Flask(__name__)
dapp = dash.Dash(__name__, server=app, url_base_pathname='/Disaster_Locator/')

@app.route("/")
@app.route("/index")
def main_page():
    return render_template('index.html')

dapp.title = "Stock Viz"

mapbox_access_token = 'pk.eyJ1IjoibmV1cmFsYWxjaGVtaXN0IiwiYSI6ImNqcWZ0Z3BuOTF4aXo0M3FwdGQ0YnllZXoifQ.xqpGQfUtBOXhKU_SYN4l5w'

map_data = pd.read_csv('./data/justintimberlake_tweets_locations.csv')
map_data = map_data[["City", "Start_Date", "Latitude", "Longitude"]].drop_duplicates()

dapp.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

dapp.layout = html.Div([ html.H2('Disaster Locator'),
    html.Div([
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'},
                                  figure={"data": [{"type": "scattermapbox",
                                                    "lat": list(map_data['Latitude']),
                                                    "lon": list(map_data['Longitude']),
                                                    "hoverinfo": "text",
                                                    "hovertext": [["City: {} <br>Latitude: {}, Longitude: {} <br>Start Date: {}".format(i,j,k,l)]
                                                                for i,j,k,l in zip(map_data['City'],map_data['Latitude'],map_data['Longitude'],map_data['Start_Date'])],
                                                    "mode": "markers",
                                                    "name": list(map_data['City']),
                                                    "marker": {
                                                        "size": 6,
                                                        "opacity": 0.7
                                                    }
                                            }],
                                            "layout": dict(autosize=True,
                                                            height=500,
                                                            font=dict(color="#191A1A"),
                                                            titlefont=dict(color="#191A1A", size='14'),
                                                            margin=dict(
                                                                l=35,
                                                                r=35,
                                                                b=35,
                                                                t=45
                                                            ),
                                                            hovermode="closest",
                                                            plot_bgcolor='#fffcfc',
                                                            paper_bgcolor='#fffcfc',
                                                            legend=dict(font=dict(size=10), orientation='h'),
                                                            title='Tweets colored by Emergency',
                                                            mapbox=dict(
                                                                accesstoken=mapbox_access_token,
                                                                style="light",
                                                                center=dict(
                                                                    lon=-73.91251,
                                                                    lat=40.7342
                                                                ),
                                                                zoom=10,
                                                            )
                                                        )
                                            }),
                        html.Div([html.A('Dashboard Credits: Adriano Yoshino', href = 'https://github.com/amyoshino/Dash_Tutorial_Series/blob/master/ex4.py')],
                            style={'text-align':'center'})
                    ], 
                ),

              
            ], className="row"
        )
    ], className='ten columns offset-by-one')