from Repo.TableRepo import TableRepo


class TableService:

    def __init__(self, date=None):
        self.repo = TableRepo(date)

    def initTable(self):
        return self.repo.initTable()

    def CautareElement(self, cnp):
        return self.repo.CautareElement(str(cnp))

    def adaugarePacient(self,coloane, inputPacient):
        self.repo.AdaugarePacient(coloane, inputPacient)