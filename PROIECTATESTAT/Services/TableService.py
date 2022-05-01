from Repo.TableRepo import TableRepo


class TableService:

    def __init__(self, date=None):
        self.repo = TableRepo(date)

    def initTable(self):
        return self.repo.initTable()

    def CautareElement(self, cnp):
        return self.repo.cautareElement(str(cnp))

    def adaugarePacient(self, coloane, inputPacient):
        self.repo.adaugarePacient(coloane, inputPacient)

    def modificarePacient(self, coloane, index, inputPacient):
        self.repo.modificarePacient(coloane, index, inputPacient)
