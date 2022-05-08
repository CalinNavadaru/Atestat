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

    def __init__(self, service, columns: list, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Adăugare Pacient")
        self.setWindowIcon(QIcon("Poze/add-user.png"))

        self.__coloane = columns
        self.__inputFields = []
        self.__service = service
        self.__buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.messageBox = None
        self.__data = None

        self.layout = QFormLayout(self)

        self.__initCampuri()

        self.layout.addWidget(self.__buttonBox)
        self.__buttonBox.accepted.connect(self.__inputUser)
        self.__buttonBox.rejected.connect(self.reject)

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
        for i in range(4, len(self.__coloane)):
            if type(userInput[i]) is None or userInput[i] == '':
                return False

        return True

    def __showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def __inputUser(self):
        self.__userInput = [x.text().strip() for x in self.__inputFields]
        if self.__validateInput(self.__userInput):
            self.__data = self.__service.AddPacient(self.__coloane, self.__userInput)
            super().accept()
        else:
            self.__showMessage()

    def __initCampuri(self):
        for x in self.__coloane:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.__inputFields.append(inputCamp)

    def getData(self):
        return self.__data
