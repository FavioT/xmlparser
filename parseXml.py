import json, xmltodict, requests, pymongo

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db

def add_players(db):
    req = requests.get("http://www.fantasybasketballnerd.com/service/players", verify=False)
    jsonData = json.dumps(xmltodict.parse(req.text))
    jsonConvert = json.loads(jsonData)
    for item in jsonConvert:
	for player in jsonConvert[item]['Player']:
	    db.all_players.insert(player)

def get_players(db):
    return db.all_players.find_one()

if __name__ == '__main__':
    db = get_db()
    add_players(db)
    print get_players(db)