import datetime

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox

from UI.MessageWindow import MessageWindow


def isdate(date):
    try:
        datetime.datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False


class AddPacientWindow(QDialog):

    def __init__(self, service, coloane: list, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Adăugare Pacient")
        self.setWindowIcon(QIcon("Poze/add-user.png"))

        self.coloane = coloane
        self.campuri = []
        self.service = service
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.messageBox = None
        self.data = None

        self.layout = QFormLayout(self)

        self.initCampuri()

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
        if not isdate(userInput[3]):
            return False
        for i in range(4, len(self.coloane)):
            if type(userInput[i]) is None or userInput[i] == '':
                return False

        return True

    def showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def inputUser(self):
        userInput = [x.text() for x in self.campuri]
        if self.__validateInput(userInput):
            self.data = self.service.AddPacient(self.coloane, userInput)
            super().accept()
        else:
            self.showMessage()

    def initCampuri(self):
        for x in self.coloane:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.campuri.append(inputCamp)

    def getData(self):
        return self.data
