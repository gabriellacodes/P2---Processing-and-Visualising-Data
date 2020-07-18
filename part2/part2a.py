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

x_values = []
y_values_min = []
y_values_max = []
for forecast in data["DailyForecasts"]:
    x_values.append(convert_date(forecast["Date"]))
    y_values_min.append(convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]))
    y_values_max.append(convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]))

fig = px.Figure()
fig.add_trace(px.Scatter(
                x=x_values,
                y=y_values_max,
                name = 'Maximum Temperature',
                mode = "lines+markers",
                line = dict(color="#FF9326")
                ))
fig.add_trace(px.Scatter(
                x=x_values,
                y=y_values_min,
                name = 'Minimum Temperature',
                mode = "lines+markers",
                line = dict(color="#2693FF")
                ))
fig.update_layout(
    title="Historical Temperature Overview (Part 2a)",
    xaxis_title="Date",
    yaxis_title="Temperature (in °C)",
    legend_title="Legend",
)
fig.show()

## An alternative, just doesn't give series titles and it needs to use plotly.express and not plotly.graph_objects ##
# fig = px.line(
#     df,
#     x="Date",
#     y=[y_values_max,y_values_min],
#     labels = {
#         "value": "Temperature (in °C)",
#         "variable": "Legend",
#         "wide_variable_0": "Maximum Temperature"
#     },
#     title='Historical Temperature Overview (Part 2a)'
# )
# fig.show()
