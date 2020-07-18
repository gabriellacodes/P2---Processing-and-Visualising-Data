import json
import plotly.graph_objects as px
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

fig = px.Figure()
fig.add_trace(px.Scatter(
                x=x_values_min,
                y=y_values_min,
                name = 'Minimum Temperature',
                mode = "lines+markers",
                line = dict(color="#A64DFF")
                ))
fig.add_trace(px.Scatter(
                x=x_values_min,
                y=y_values_min_real,
                name = 'Minimum "Real Feel" Temperature',
                mode = "lines+markers",
                line = dict(color="#FF73FF")
                ))
fig.add_trace(px.Bar(
                x=x_values_min,
                y=y_values_min_real_shade,
                name = 'Minimum "Real Feel Shade" Temperature'
                ))
fig.update_layout(
    title="Historical Temperature Overview (Part 2b)",
    xaxis_title="Date",
    yaxis_title="Temperature (in °C)",
    legend_title="Legend",
)
fig.show()

## An alternative, just doesn't give series titles and it needs to use plotly.express and not plotly.graph_objects ##
# fig1 = px.line(
#     df_min,
#     x="Date",
#     y=[y_values_min,y_values_min_real,y_values_min_real_shade],
#     labels = {
#         "value": "Temperature (in °C)"
#     },
#     title='Historical Temperature Overview (Part 2b)'
# )
# fig1.show()

