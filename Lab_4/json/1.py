import json

json_file_path = '/Users/telma/Desktop/PP2_summer_2024/Lab_4/json/sample-data.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)  
    

print(data)
