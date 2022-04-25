import pymongo as mongo


client = mongo.MongoClient("mongodb://localhost:27017/")

# b = client["Atestat"]

# col = db["test"]

# mydict = {"name": "ma-ta", "address": "Highway 36"}

# x = col.insert_one(mydict)

# print(client.list_database_names())


class Backend:
    def __init__(self):
        self.db = client["Atestat"]
        self.col = self.db["Pacienti"]

    def afisare_pacienti(self):
        lista = self.col.find()
        for x in lista:
            print(x)

    #def update_pacienti(self):
