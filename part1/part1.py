import json
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    return f"{temp}{DEGREE_SYMBOL}"

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    return round((temp_in_farenheit - 32)*(5/9),1)

def calculate_mean(total, num_items):
    return round((total / num_items),1)

def process_weather(forecast_file):
    with open(forecast_file,"r") as read_file:
        data = json.load(read_file)
    # How many days in dataset
    num_days_in_data = len(data["DailyForecasts"])
    # The overall min temperature, and the date this will occur.
    min_list = []
    for forecast in data["DailyForecasts"]:
        min_list.append([convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]),convert_date(forecast["Date"])])
    min_list.sort()
    # The overall max temperature, and the date this will occur.
    max_list = []
    for forecast in data["DailyForecasts"]:
        max_list.append([convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]),convert_date(forecast["Date"])])
    max_list.sort()
    # The mean minimum temperature.
    total_min = 0
    num_items_min = 0
    for forecast in data["DailyForecasts"]:
        total_min = total_min + (convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]))
        num_items_min = num_items_min + 1
    ave_min = round(calculate_mean(total_min,num_items_min),1)
    # The mean maximum temperature.
    total_max = 0
    num_items_max = 0
    for forecast in data["DailyForecasts"]:
        total_max = total_max + (convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]))
        num_items_max = num_items_max + 1
    ave_max = round(calculate_mean(total_max,num_items_max),1)

    daystring = ""
    for forecast in data["DailyForecasts"]:
        daystring = daystring + f'-------- {convert_date(forecast["Date"])} --------\nMinimum Temperature: {format_temperature(convert_f_to_c(forecast["Temperature"]["Minimum"]["Value"]))}\nMaximum Temperature: {format_temperature(convert_f_to_c(forecast["Temperature"]["Maximum"]["Value"]))}\nDaytime: {forecast["Day"]["LongPhrase"]}\n    Chance of rain:  {forecast["Day"]["RainProbability"]}%\nNighttime: {forecast["Night"]["LongPhrase"]}\n    Chance of rain:  {forecast["Night"]["RainProbability"]}%\n\n'

    return f'{num_days_in_data} Day Overview\n    The lowest temperature will be {format_temperature(min_list[0][0])}, and will occur on {min_list[0][1]}.\n    The highest temperature will be {format_temperature(max_list[-1][0])}, and will occur on {max_list[-1][1]}.\n    The average low this week is {format_temperature(ave_min)}.\n    The average high this week is {format_temperature(ave_max)}.\n\n{daystring}'

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





