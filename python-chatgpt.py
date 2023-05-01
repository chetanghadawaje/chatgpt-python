import requests
from confing import *


HEADERS = {"Content-Type": "application/json",
           "Authorization": f"Bearer {API_KEY}"}

que = input("Enter your query: ")

request_data = {
  "model": "text-davinci-003",
  "prompt": que,
  "max_tokens": 50,
  "temperature": 0.5,
}

response = requests.post(API_END_POINT, headers=HEADERS, json=request_data)

if response.status_code == 200:
    response_data = response.json()
    print(f"{response_data}")
    print("*"*80)
    for data in response_data.get("choices"):
        print(f"{data.get('text')}")
else:
    print(f"Error[{response.status_code}]: {response.json()}")
