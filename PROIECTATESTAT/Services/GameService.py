from Repo.GameRepo import GameRepo


class GameService:

    def __init__(self, intrebare, raspuns):
        self.__repo = GameRepo(intrebare, raspuns)

    def verif_raspuns(self):
        return self.__repo.verificareRaspunsuri()
