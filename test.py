import json

with open("settings.json", "r") as read_file:
    data = json.load(read_file)

if user_id in data["mods"]:
    print("test done")
 
 
 
 
 
 
 