from datetime import datetime

import pymongo as mongo


class TableRepo:

    def __init__(self, date=None):
        self.__client = mongo.MongoClient("mongodb://localhost:27017/")
        self.__db = self.__client["Atestat"]
        self.__col = self.__db["Pacienti"]
        self.__data = []

    def initTable(self):
        mydoc = self.__col.find()
        newdata = []
        k = 1
        for x in mydoc:
            x.pop('_id')
            temp = datetime.strptime(x['Data nasterii'], '%d-%m-%Y')
            x['Data nasterii'] = temp.strftime("%d-%m-%Y")
            newdata.append(x)
            myquery = {"CNP": x['CNP']}
            mydoc2 = {'$set': {'id': str(k)}}
            self.__col.update_one(myquery, mydoc2)
            x['id'] = k
            k += 1
            self.__data.append(x)

        return newdata

    def SearchPacient(self, cnp: str):
        for x in self.__data:
            if x['CNP'] == cnp:
                return x['id']
        return None

    def AddPacient(self, coloane: list, inputPacient: list):
        mydoc = {}
        for i in range(0, 7):
            mydoc[coloane[i]] = inputPacient[i]
        mydoc['id'] = len(self.__data) + 1
        self.__data.append(mydoc)
        self.__col.insert_one(mydoc)
        return mydoc

    def updatePacient(self, coloane: list, index, Pacient: list):
        oldPacient = {}
        mydoc = self.__col.find()
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
        self.__data[k] = newPacient
        self.__col.update_one(oldPacient, {"$set": newPacient})

    def deletePacient(self, cnp: str):
        linie = None
        mydoc = {"CNP": cnp}
        for x in self.__col.find(mydoc):
            linie = int(x['id'])
        self.__col.delete_one(mydoc)
        return linie

    def getData(self):
        return self.__data
