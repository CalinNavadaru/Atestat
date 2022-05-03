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

    def modificarePacient(self, coloane, index, inputPacient):
        self.repo.modificarePacient(coloane, index, inputPacient)

    def stergereElement(self, cnp):
        return self.repo.stergereElement(cnp)

    def getLenData(self):
        return len(self.data)
