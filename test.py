import datetime
import json
import pytz








# def time(name):
#     with open("times.json", "r") as read_file:
#         data = json.load(read_file)
#     try:
#         return (data[name])
#     except:
#         return "error"
    
# print(time("bayon"))

cest_timezone = pytz.timezone('Europe/Berlin')
cest_time = datetime.datetime.now(cest_timezone).strftime('%H:%M:%S')

print("CEST Time:", cest_time)