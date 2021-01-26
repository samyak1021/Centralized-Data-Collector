import requests
import json
import os
from datetime import datetime
response = requests.get("https://api.data.gov.in/resource/28584657-445c-4ca0-857c-de1ae6a4888c?api-key=579b464db66ec23bdd0000019b990dd666564ef24abe53890cb520c3&format=json&offset=0&limit=500")
last_updated = []
json_data = response.json()
last_updated_date = json_data["updated_date"]
last_updated.append(last_updated_date)
length = len(last_updated)
if length != 1 and last_updated[length-1] != last_updated[length-2]:
    records = json_data['records']
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    dir_path = os.path.join('F:\Data') #Folder Where you want to save data
    with open(os.path.join(dir_path, 'B' + timestr), 'w') as json_file: #File name base on current timestamp
        json.dump(records,json_file)