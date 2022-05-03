from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox


class AddPacientWindow(QDialog):

    def __init__(self, service, coloane: list, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Adaugare Pacient")
        self.setWindowIcon(QIcon("add-user.png"))

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
        for x in userInput:
            if x  == '':
                return False

        return True

    def showMessage(self):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowIcon(QIcon("icons8-information-48.png"))
        self.messageBox.setIcon(QMessageBox.Warning)
        self.messageBox.setWindowTitle("Eroare!")
        self.messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.messageBox.setEscapeButton(QMessageBox.Close)
        self.messageBox.setFont(QFont("Times", 10))
        self.messageBox.resize(self.messageBox.sizeHint())
        self.messageBox.setText("Ati introdus o valoare gresita/invalida!")
        self.messageBox.exec()
        self.messageBox.hide()

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
