import pymongo as mongo


client = mongo.MongoClient("mongodb://localhost:27017/")


class TableRepo:

    def __init__(self, date = None):
        self.db = client["Atestat"]
        self.col = self.db["Pacienti"]
        self.date = []

    def initTable(self):
        mydoc = self.col.find()
        for x in mydoc:
            x.pop('_id')
            self.date.append(x)

        return self.date


