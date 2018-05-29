import json, xmltodict, requests
from pymongo import MongoClient

def get_db():
    client = MongoClient('localhost:27017')
    db = client.fantasy
    return db

def add_teams(db):
    req = requests.get("http://www.fantasybasketballnerd.com/service/teams", verify=False)
    jsonData = json.dumps(xmltodict.parse(req.text))
    jsonConvert = json.loads(jsonData)
    for item in jsonConvert:
        for team in jsonConvert[item]['Team']:
            db.all_teams.insert(team)

def add_players(db):
    req = requests.get("http://www.fantasybasketballnerd.com/service/players", verify=False)
    jsonData = json.dumps(xmltodict.parse(req.text))
    jsonConvert = json.loads(jsonData)
    for item in jsonConvert:
        for player in jsonConvert[item]['Player']:
            db.all_players.insert(player)

def get_players(db):
    return db.all_players.find_one()

def get_teams(db):
    return db.all_teams.find_one()

if __name__ == '__main__':
    db = get_db()
    add_players(db)
    add_teams(db)
    print get_players(db)
    print get_teams(db)
