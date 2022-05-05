from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel, QMessageBox

from UI.AddPacientWindow import isdate
from UI.MessageWindow import MessageWindow


class UpdateWindow(QDialog):

    def __init__(self, service, coloane: list, nrPacienti: int, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Modificare Pacient")
        self.setWindowIcon(QIcon("Poze/icons8-user-24.png"))

        self.messageBox = None
        self.nrPacienti = nrPacienti
        self.coloane = coloane
        self.campuri = []
        self.userInput = []
        self.index = None
        self.service = service
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout = QFormLayout(self)
        self.initLayout()

        self.layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.inputUser)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def __validateInput(self, userInput):
        if type(userInput[0]) != str or type(userInput[1]) != str:
            return False
        if not userInput[2].isdigit() or len(userInput[2]) != 13:
            return False
        if not userInput[5].isdigit() or len(userInput[5]) != 20:
            return False
        if not isdate(userInput[3]):
            return False
        for i in range(4, len(self.coloane)):
            if type(userInput[i]) is None or userInput[i] == '':
                return False

        return True

    def inputUser(self):
        newPacient = [x.text() for x in self.campuri]
        if self.index.text() is not None and all(newPacient) == True:
            index = int(self.index.text())
            if index <= self.nrPacienti and self.__validateInput(newPacient):
                self.service.modificarePacient(self.coloane, index, newPacient)
                super().accept()
            else:
                self.showMessage()

        else:
            self.showMessage()

    def initLayout(self):
        self.index = QLineEdit(self)
        self.layout.addRow("Linie: ", self.index)

        mesaj = QLabel("Date pacient")
        self.layout.addWidget(mesaj)

        self.initCampuri()

    def initCampuri(self):
        for x in self.coloane:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.campuri.append(inputCamp)

    def showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")
