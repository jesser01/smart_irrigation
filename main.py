# -*- coding: utf-8 -*-
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import datetime
import random
from dash import  html, Input, Output, callback_context

def message(i) :
    messages = ["messages :",'we dont need to irrigate','','','','','']
    humidity = random.randint(1, 100)
    messages[6] = "temperature= " + str(random.randint(20, 45)) + '°C' + '||humidity= ' + str(humidity) + '%'
    water_level = random.randint(1, 9) * 10
    soil_moisture = random.randint(1, 100)
    if (humidity < 70) :
        if (soil_moisture < 20) :
            messages[1] ="The soil must be irrigated ."
            if (water_level > 10):
                messages[2] = "the irrigation begins ."
                activation_pomp1 = 1
            else:
                messages[3] ="the water reservoir is empty ."
                while (water_level != 100) :
                    water_level = water_level + 10
                    activation_pomp2 = 1
                    activation_pomp1 = 0
                water_level = 100
                messages[4] = "the water reservoir is full ."
                activation_pomp1 = 1
                messages[5] ="the irrigation begins ."
    else:
        messages[1]= "we Hope it rains today"
    return (messages[i])



#dashbord structure
#////////////////////////////////////////////////////////////////////
now = datetime.datetime.now()
app = dash.Dash(__name__)

colors = {
    'background': '#2E4053 ',
    'text': '#7FDBFF',
}

# assume you have a "long-form" data frame
cosomation = pd.DataFrame({
    "day": ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun'],
    "water": [100, 0, 50, 0, 20, 60, 0, ]
})
# see https://plotly.com/python/px-arguments/ for more options

fig1 = px.line(cosomation, x="day", y="water", markers=True,title='water consumption for the last week in liter ( L )',)

fig1.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background'],
                             "border": "4px #7FDBFF solid",
                             'border-radius': '10px',
                             'padding': '10px',
                             'margin': '10px',
                             }, children=[
    html.H1(
        children=now.strftime("%d/%m/%y || %H:%M"),
        style={
            'backgroundColor':'#283747 ',
            "border": "4px #7FDBFF solid",
            'border-radius': '10px',
            'padding': '30px',
            'margin': '10px',
            'textAlign': 'center',
            'display': 'inline-block', 'vertical-align': 'top', 'margin-left': '3vw', 'margin-top': '3vw',
            'color': colors['text']
        }
    ),


    html.Div([html.H3(message(0)),
             html.P(message(1)),
             html.P(message(2)),
             html.P(message(3)),
             html.P(message(4)),
             html.P(message(5)),

             ],style={
        'backgroundColor':'#283747',
        'position': 'absolute',
        'font-size': '30px',
        'width': '680px',
        'height': '450px',
        "border": "4px #7FDBFF solid",
        'border-radius': '10px',
        'textAlign': 'left',
        'padding': '5px',
        'margin': '10px',
        'display': 'inline-block',
        'margin-top': '170px',
        'margin-left': '250px',
        'margin-right': '50px',
        'margin-bottom':'10px',
        'color': colors['text']
    }),
    html.Div([html.H1(message(6))


    ],style={'backgroundColor': '#283747',
              "border": "4px #7FDBFF solid",
              'border-radius': '10px',
              'height':'40px',
              'padding': '30px',
              'margin': '10px',
              'textAlign': 'center',
              'display': 'inline-block', 'vertical-align': 'top', 'margin-right': '10', 'margin-top': '3vw',
              'color': colors['text']
              }),
    html.Div(style={'backgroundColor':'#283747 ',
                    'position':'relative',
                    'font-size': '30px',
                    'width': '500px',
                    "border": "4px #7FDBFF solid",
                    'border-radius': '10px',
                    'padding': '5px',
                    'margin': '10px',
                    'display': 'inline-block',
                    'margin-top': '20px',
                    'margin-right': '900px',
                    'margin-bottom': '0px',
                    },
             children=[
                 dcc.Graph(
                     id='example-graph-1',
                     figure=fig1
                 )
             ]),

])


if __name__ == '__main__':
    app.run_server(debug=True)