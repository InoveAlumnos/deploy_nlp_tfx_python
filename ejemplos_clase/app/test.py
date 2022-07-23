import requests
import json

url = "http://localhost:8501/v1/models/chatbot:predict"
payload = {"instances": [["Hola!"]]}

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
print(response.text)
