import requests
import json

city = input("Enter the name of the city : ")
url = f"https://api.weatherapi.com/v1/current.json?key=271272cec52244cc818180234231310&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
