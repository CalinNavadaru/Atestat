import pymongo as mongo

client = mongo.MongoClient("mongodb://localhost:27017/")


class TableRepo:

    def __init__(self, date=None):
        self.db = client["Atestat"]
        self.col = self.db["Pacienti"]
        self.data = []

    def initTable(self):
        mydoc = self.col.find()
        newdata = []
        k = 1
        for x in mydoc:
            x.pop('_id')
            newdata.append(x)
            x['id'] = k
            k += 1
            self.data.append(x)

        return newdata

    def CautareElement(self, cnp: str):
        for x in self.data:
            if x['CNP'] == cnp:
                return x['id']
        return None
