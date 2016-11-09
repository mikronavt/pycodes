import requests
import sys
import json

for number in sys.stdin:
    r = "http://numbersapi.com/" + number.strip() + "/math?json=true"
    json_str = requests.get(r).text
    s = json.loads(json_str)
    print(["Boring","Interesting"][s['found']])