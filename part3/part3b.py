import json
from datetime import datetime

with open("data/historical_6hours.json","r") as read_file:
        data = json.load(read_file)

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"

def convert_time(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%I:%M%p")

total_precip = 0
hours_rained = 0
temp = []
uv_index = []
daylight_hours = 0
for forecast in data:
    # Storing temperatures
    temp.append([forecast["Temperature"]["Metric"]["Value"],convert_time(forecast["LocalObservationDateTime"])])
    # Calculating total precipitation
    total_precip = total_precip + forecast["Precip1hr"]["Metric"]["Value"]
    # Count for how many hours it rained
    if forecast["PrecipitationSummary"]["PastHour"]["Metric"]["Value"] > 0:
        hours_rained = hours_rained + 1
    else:
        hours_rained = hours_rained
    # Number of daylight hours recorded
    if forecast["IsDayTime"] == True:
        daylight_hours = daylight_hours + 1
    else:
        daylight_hours = daylight_hours
    # Store UV Index
    uv_index.append([forecast["UVIndex"],convert_time(forecast["LocalObservationDateTime"])])
temp.sort()
uv_index.sort()

max_uv = uv_index[-1]
max_uv_times = []
for x in uv_index:
    if x[0] >= max_uv[0]:
        max_uv.append(x)
        max_uv_times.append(x[1])
max_uv_times = ', '.join(max_uv_times)

max_temp = temp[-1]
max_temp_times = []
for x in temp:
    if x[0] >= max_temp[0]:
        max_temp.append(x)
        max_temp_times.append(x[1])
max_temp_times = ', '.join(max_temp_times)

min_temp = temp[0]
min_temp_times = []
for x in temp:
    if x[0] <= min_temp[0]:
        min_temp.append(x)
        min_temp_times.append(x[1])
min_temp_times = ', '.join(min_temp_times)

with open("Weather_Summary.txt","w") as file:
    file.write(f"The minimum temperature in this dataset is {format_temperature(min_temp[0])}, which occurs at {min_temp_times}. The maximum temperature in this dataset is {format_temperature(max_temp[0])}, which occurs at {max_temp_times}. {total_precip}mm of precipitation fell over a period of {hours_rained} hours during this dataset. In this dataset there were {daylight_hours} hours of daylight with a maximum UV index of {max_uv[0]} occuring at {max_uv_times}.")