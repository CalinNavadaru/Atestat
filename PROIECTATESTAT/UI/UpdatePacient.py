from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel

from UI.AddPacientWindow import isdate
from UI.MessageWindow import MessageWindow


class UpdateWindow(QDialog):

    def __init__(self, service, columns: list, nrPacienti: int, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Modificare Pacient")
        self.setWindowIcon(QIcon("Poze/icons8-user-24.png"))

        self.messageBox = None
        self.__nrPacienti = nrPacienti
        self.__columns = columns
        self.__inputFields = []
        self.__userInput = []
        self.__index = None
        self.__newPacient = None
        self.__service = service
        self.__buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout = QFormLayout(self)
        self.__initLayout()

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
        for i in range(4, len(self.__columns)):
            if type(userInput[i]) is None or userInput[i] == '':
                return False

        return True

    def __inputUser(self):
        self.__newPacient = [x.text() for x in self.__inputFields]
        if self.__index.text() is not None and all(self.__newPacient) == True:
            index = int(self.__index.text())
            if index <= self.__nrPacienti and self.__validateInput(self.__newPacient):
                self.__service.updatePacient(self.__columns, index, self.__newPacient)
                super().accept()
            else:
                self.__showMessage()

        else:
            self.__showMessage()

    def __initLayout(self):
        self.__index = QLineEdit(self)
        self.layout.addRow("Linie: ", self.__index)

        mesaj = QLabel("Date pacient")
        self.layout.addWidget(mesaj)

        self.__initCampuri()

    def __initCampuri(self):
        for x in self.__columns:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.__inputFields.append(inputCamp)

    def __showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")
