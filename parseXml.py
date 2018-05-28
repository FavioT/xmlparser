import json, xmltodict, requests

req = requests.post("https://www.fantasybasketballnerd.com/service/players")

print(json.dumps(xmltodict.parse(req.text), indent=4))
