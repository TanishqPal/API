import requests
import json

url = "https://restcountries.com/v3.1/all?fields=name,population,area"

response = requests.get(url)
data = response.json()

new_data = []

for item in data:
    common_name = item['name']['common']
    area = item['area']
    population = item['population']
    new_item = {
        'name': common_name,
        'area': area,
        'population': population
    }
    new_data.append(new_item)

new_json_data = json.dumps(new_data, indent=2)

with open("countrypoparea.json", 'w') as json_file:
    json.dump(new_data, json_file, indent=2)
