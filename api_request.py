import requests
import json
from unidecode import unidecode

seatgeek_return = json.loads(requests.get("http://api.seatgeek.com/2/events").text)

json.dump(seatgeek_return,open("seatgeek.json","w"))

seatgeek = json.load(open("seatgeek.json","r"))

for event in seatgeek["events"]:
    print event["venue"]
