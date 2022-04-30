from Repo.TableRepo import TableRepo


class TableService:

    def __init__(self, date=None):
        self.repo = TableRepo(date)

    def initTable(self):
        return self.repo.initTable()
