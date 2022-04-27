import os


class GameRepo:

    def __init__(self, intrebare, raspuns):
        self.raspunsuri = []
        self.init_raspunsuri()
        self.intrebare = intrebare
        self.raspuns = raspuns

    def init_raspunsuri(self):
        path_to_file = os.path.join(os.path.dirname(__file__), "Raspunsuri.txt")
        f = open(path_to_file)
        for x in f:
            x = x.strip()
            self.raspunsuri.append(x)

    def verificareRaspunsuri(self):
        return self.raspuns == self.raspunsuri[self.intrebare - 1]
