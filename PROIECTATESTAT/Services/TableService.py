from Repo.TableRepo import TableRepo


class TableService:

    def __init__(self, date=None):
        self.repo = TableRepo(date)
        self.data = None

    def initTable(self):
        self.data = self.repo.initTable()
        return self.data

    def SearchPacient(self, cnp):
        return self.repo.SearchPacient(str(cnp))

    def AddPacient(self, coloane, inputPacient):
        return self.repo.AddPacient(coloane, inputPacient)

    def updatePacient(self, coloane, index, inputPacient):
        self.repo.updatePacient(coloane, index, inputPacient)

    def deletePacient(self, cnp):
        return self.repo.deletePacient(cnp)

    def getLenData(self):
        return len(self.data)

    def getData(self):
        return self.repo.getData()
