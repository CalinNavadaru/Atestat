import os


class GameRepo:

    def __init__(self, intrebare, raspuns):
        self.__raspunsuri = []
        self.__init_raspunsuri()
        self.__intrebare = intrebare
        self.__raspuns = raspuns

    def __init_raspunsuri(self):
        path_to_file = os.path.join(os.path.dirname(__file__), "Raspunsuri.txt")
        f = open(path_to_file)
        for x in f:
            x = x.strip()
            self.__raspunsuri.append(x)

    def verificareRaspunsuri(self):
        return self.__raspuns == self.__raspunsuri[self.__intrebare - 1]
