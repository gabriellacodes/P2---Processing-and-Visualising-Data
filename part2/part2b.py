import json
import plotly.express as px
import pandas as pd
from datetime import datetime

with open("data/forecast_5days_a.json","r") as read_file:
        data = json.load(read_file)

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    return round((temp_in_farenheit - 32)*(5/9),1)

x_values_min = []
y_values_min = []
y_values_min_real = []
y_values_min_real_shade = []
for forecast in data["DailyForecasts"]:
    x_values_min.append(convert_date(forecast["Date"]))
    y_values_min.append(convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]))
    y_values_min_real.append(convert_f_to_c(forecast["RealFeelTemperature"]["Minimum"]["Value"]))
    y_values_min_real_shade.append(convert_f_to_c(forecast["RealFeelTemperatureShade"]["Minimum"]["Value"]))

df_min = {
    "Date": x_values_min,
}

fig1 = px.line(
    df_min,
    x="Date",
    y=[y_values_min,y_values_min_real,y_values_min_real_shade],
    labels = {
        "value": "Temperature (in °C)"
    },
    title='Historical Temperature Overview (Part 2b)'
)
fig1.show()

