from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel, QMessageBox


class UpdateWindow(QDialog):

    def __init__(self, service, coloane : list,nrPacienti : int, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Modificare Pacient")
        self.setWindowIcon(QIcon("icons8-user-24.png"))

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
        for x in userInput:
            if x  == '':
                return False

        return True

    def inputUser(self):
        newPacient = [x.text() for x in self.campuri]
        index = int(self.index.text())
        if index <= self.nrPacienti and self.__validateInput(newPacient):
            self.service.modificarePacient(self.coloane, index, newPacient)
            super().accept()
        else:
            self.showMessage()

    def initLayout(self):
        self.index = QLineEdit(self)
        self.layout.addRow("Linie: " , self.index)

        mesaj = QLabel("Date pacient")
        self.layout.addWidget(mesaj)

        self.initCampuri()

    def initCampuri(self):
        for x in self.coloane:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.campuri.append(inputCamp)

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
