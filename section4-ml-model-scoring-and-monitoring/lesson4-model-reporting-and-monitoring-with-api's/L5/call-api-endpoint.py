import subprocess
from subprocess import DEVNULL, STDOUT, check_call
import requests

#### Command-line solution####
response1=subprocess.run(['curl', '127.0.0.1:8000?user=brad'],capture_output=True).stdout
print(response1)

response2=subprocess.run(['curl', '127.0.0.1:8000/summary?filename=testdata.csv'],capture_output=True).stdout
print(response2)

response3=subprocess.run(['curl', '127.0.0.1:8000/size?filename=testdata.csv'],capture_output=True).stdout
print(response3)

#### Request module solution####
response4=requests.get('http://127.0.0.1:8000?user=brad').content
print(response4)

response5=requests.get('http://127.0.0.1:8000/summary?filename=testdata.csv').content
print(response5)

response6=requests.get('http://127.0.0.1:8000/size?filename=testdata.csv').content
print(response6)