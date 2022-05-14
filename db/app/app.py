import json
from pymongo import MongoClient

FILE = 'offline_.json'


def writeCSVtoDB(File,tableDB):


    file = open(File, 'r',encoding="utf8")
    data = json.load(file)
    for i in data:
        data[i]["_id"] = i
        print(data[i])
        tableDB.insert_one(data[i])
    file.close()
    print("DONE", File)


def get_database():
    client = MongoClient('mongo', 27017 ,username='admin', password='admin')
    print("DataBase Created")
    return client['iot']


def get_table(db,table):
    print("Table:",table,"created!")
    return db[table]


if __name__ == "__main__":
    db = get_database()
    dbTable = get_table(db,'offline')
    writeCSVtoDB(FILE,dbTable)