import requests
import json
import os

#Specify a URL that resolves to your workspace
URL = "http://127.0.0.1:8000/"

with open('config.json','r') as f:
    config = json.load(f) 

test_data_path = config["test_data_path"]
output_model_path = config["output_model_path"]
test_data_name = config["test_data_name"]
api_return_name = config["api_return_name"]

test_data_file_path = os.path.join(test_data_path, test_data_name)
api_return_path = os.path.join(output_model_path, api_return_name)

#Call each API endpoint and store the responses
response1 = requests.post(URL + 'prediction', data={'path': json.dumps(test_data_file_path)})
response2 = requests.get(URL + 'scoring')
response3 = requests.get(URL + 'summarystats')
response4 = requests.get(URL + 'diagnostics')

#combine all API responses
responses = {
    'prediction': response1.json(),
    'scoring': response2.json(),
    'summarystats': response3.json(),
    'diagnostics': response4.json()
}

#write the responses to your workspace
with open(api_return_path, 'w') as f:
    json.dump(responses, f)


