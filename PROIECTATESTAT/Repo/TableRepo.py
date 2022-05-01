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
            myquery = {"CNP" : x['CNP']}
            mydoc2 = {'$set' : {'id' : str(k)}}
            self.col.update_one(myquery, mydoc2)
            x['id'] = k
            k += 1
            self.data.append(x)

        return newdata

    def cautareElement(self, cnp: str):
        for x in self.data:
            if x['CNP'] == cnp:
                return x['id']
        return None

    def adaugarePacient(self, coloane: list, inputPacient: list):
        mydoc = {}
        for i in range(0, 7):
            mydoc[coloane[i]] = inputPacient[i]
        mydoc['id'] = len(self.data)
        self.data.append(mydoc)
        self.col.insert_one(mydoc)

    def modificarePacient(self, coloane: list, index, Pacient: list):
        oldPacient = {}
        mydoc = self.col.find()
        k = 0
        for x in mydoc:
            k += 1
            if k == index:
                oldPacient = x
                break
        newPacient = {}
        for i in range(0, 7):
            newPacient[coloane[i]] = Pacient[i]
        if k < index:
            return
        self.col.update_one(oldPacient, {"$set": newPacient})

    def stergereElement(self, cnp: str):
        linie = None
        mydoc = {"CNP": cnp}
        for x in self.col.find(mydoc):
            linie = int(x['id'])
        self.col.delete_one(mydoc)
        return linie
