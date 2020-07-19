import json
import plotly.graph_objects as px
from datetime import datetime
from collections import Counter

with open("data/historical_24hours_b.json","r") as read_file:
        data = json.load(read_file)

## Keeping here for future :) ##
# def convert_time(iso_string):
#     d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
#     # handy!! https://www.programiz.com/python-programming/datetime/strftime
#     return d.strftime('%-I%p')
# time = []
# for forecast in data:
#     temp.append(convert_time(forecast["LocalObservationDateTime"]))

## Deriving boxplots ##
temp = []
for forecast in data:
    temp.append(forecast["Temperature"]["Metric"]["Value"])

temp_rf = []
for forecast in data:
    temp_rf.append(forecast["RealFeelTemperature"]["Metric"]["Value"])

fig1 = px.Figure()
fig1.add_trace(px.Box(
                x = temp,
                name = "Temperature"
                ))
fig1.add_trace(px.Box(
                x = temp_rf,
                name = "Real Feel Temperature"
                ))
fig1.update_layout(
                title = "Box Plots of Temperature Data",
                xaxis_title = "Temperature (in °C)",
                showlegend = False
)
fig1.show()

## Deriving bar graph ##
weathertext_statuses = []
for status in data:
    weathertext_statuses.append(status["WeatherText"])
weathertext_statuses = dict(Counter(weathertext_statuses))

x_values = []
y_values = []
for text, count in weathertext_statuses.items():
    x_values.append(text)
    y_values.append(count)
fig2 = px.Figure()
fig2.add_trace(px.Bar(
                y=y_values,
                x=x_values
                ))
fig2.update_layout(
                title="Weather Status Occurences per Hour",
                xaxis_title="Weather Status",
                yaxis_title="Occurrences on Hourly Basis"
)
fig2.show()
