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

dapp.title = "Emergency Tweet Dashboard"

mapbox_access_token = 'pk.eyJ1IjoibmV1cmFsYWxjaGVtaXN0IiwiYSI6ImNqcWZ0Z3BuOTF4aXo0M3FwdGQ0YnllZXoifQ.xqpGQfUtBOXhKU_SYN4l5w'

map_data = pd.read_csv('data/map_data.csv')

map_data_on = map_data[map_data['label'] == 'on-topic']
map_data_off = map_data[map_data['label'] == 'off-topic']

map_data_off = map_data_off[["label", "tweet", "lat", "long"]].drop_duplicates()
map_data_on = map_data_on[["label", "tweet", "lat", "long"]].drop_duplicates()

dapp.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})

dapp.layout = html.Div([ html.H2('Disaster Locator'),
    html.Div([
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'},
                                  figure={"data": [{"type": "scattermapbox",
                                                    "lat": list(map_data_off['lat']),
                                                    "lon": list(map_data_off['long']),
                                                    "hoverinfo": "text",
                                                    "hovertext": [[f"Label: {i} <br>Latitude: {j}, Longitude: {k} <br>Tweet: {l}"]
                                                                for i,j,k,l in zip(map_data_off['label'],map_data_off['lat'],map_data_off['long'],map_data_off['tweet'])],
                                                    "mode": "markers",
                                                    "name": 'Off-Topic',
                                                    "marker": {
                                                        "size": 6,
                                                        "opacity": 0.3
                                                    },
                                                   },
                                                    {"type": "scattermapbox",
                                                    "lat": list(map_data_on['lat']),
                                                    "lon": list(map_data_on['long']),
                                                    "hoverinfo": "text",
                                                    "hovertext": [[f"Label: {i} <br>Latitude: {j}, Longitude: {k} <br>Tweet: {l}"]
                                                                for i,j,k,l in zip(map_data_on['label'],map_data_on['lat'],map_data_on['long'],map_data_on['tweet'])],
                                                    "mode": "markers",
                                                    "name": 'On-Topic',
                                                    "marker": {
                                                        "size": 6,
                                                        "opacity": 0.7,
                                                        "color": '#ff0040'
                                                    }
                                                    }],
                                            "layout": dict(autosize=True,
                                                            height=750,
                                                            font=dict(color="#191A1A"),
                                                            titlefont=dict(color="#191A1A", size='24'),
                                                            margin=dict(
                                                                l=35,
                                                                r=35,
                                                                b=35,
                                                                t=45
                                                            ),
                                                            hovermode="closest",
                                                            plot_bgcolor='#fffcfc',
                                                            paper_bgcolor='#fffcfc',
                                                            legend=dict(font=dict(size=15), orientation='h'),
                                                            title='Tweets Colored by Emergency',
                                                            mapbox=dict(
                                                                accesstoken=mapbox_access_token,
                                                                style="light",
                                                                center=dict(
                                                                    lon=-117.358385,
                                                                    lat=33.996447
                                                                ),
                                                                zoom=10,
                                                            )
                                                        )
                                            }),
                        html.Div([html.A('Dashboard Credits: Ben Liu, Chris Sinatra, Connie Tiet, and Mike Hong', href = 'https://github.com/csinatra/Twitter-Disaster-Repo')],
                            style={'text-align':'center'}),
                        html.Div([html.A('Dashboard Inspiration: Adriano Yoshino', href = 'https://github.com/amyoshino/Dash_Tutorial_Series/blob/master/ex4.py')],
                            style={'text-align':'center'})

                    ],
                ),


            ], className="row"
        )
    ], className='ten columns offset-by-one')
