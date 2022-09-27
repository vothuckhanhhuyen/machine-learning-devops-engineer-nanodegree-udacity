import subprocess
import requests

response=subprocess.run(['curl', '127.0.0.1:8000/prediction'],capture_output=True).stdout

response2=requests.get('http://127.0.0.1:8000/prediction').content

print(response)
print(response2)