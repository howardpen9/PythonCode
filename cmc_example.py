from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "10", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "2db7b8c6-e6f2-4b9c-a293-a0dba9742a75",
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


print(json.dumps(data, indent=2))
