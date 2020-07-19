import json
from datetime import datetime

with open("data/historical_6hours.json","r") as read_file:
        data = json.load(read_file)

def convert_time(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%I:%M%p")

total_precip = 0
hours_rained = 0
temp = []
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
    
temp.sort()
print(temp)

# with open("Weather_Summary.txt","w") as file:
    # file.write(f'x')