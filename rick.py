import requests
import json


url = "http://open-api.bybt.com/"

payload = {}

headers = {
  'bybtSecret': '963890f42449495d995162ebe30224b4'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

