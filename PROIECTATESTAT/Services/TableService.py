from Repo.TableRepo import TableRepo


class TableService:

    def __init__(self, date=None):
        self.__repo = TableRepo(date)
        self.__data = None

    def initTable(self):
        self.__data = self.__repo.initTable()
        return self.__data

    def SearchPacient(self, cnp):
        return self.__repo.SearchPacient(str(cnp))

    def AddPacient(self, coloane, inputPacient):
        return self.__repo.AddPacient(coloane, inputPacient)

    def updatePacient(self, coloane, index, inputPacient):
        self.__repo.updatePacient(coloane, index, inputPacient)

    def deletePacient(self, cnp):
        return self.__repo.deletePacient(cnp)

    def getLenData(self):
        return len(self.getData())

    def getData(self):
        self.__data = self.__repo.getData()
        return self.__data
