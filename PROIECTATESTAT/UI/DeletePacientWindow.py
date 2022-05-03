from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel, QMessageBox


class DeletePacientWindow(QDialog):

    def __init__(self, service, coloane, parent=None):
        super().__init__(parent)
        self.service = service
        self.coloane = coloane
        self.linie = None
        self.messageBox = None
        self.setWindowTitle("Stergere Pacient")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)

        self.cnp = QLineEdit(self)
        mesaj = QLabel("Introduceti datele pacientului:")
        layout.addWidget(mesaj)
        layout.addRow("CNP Pacient:", self.cnp)

        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.inputUser)
        buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def findCNP(self):
        data = self.service.getData()
        for x in data:
            if x['CNP'] == self.cnp.text():
                return True

        return False

    def validateCNP(self):
        return self.cnp.text() != '' and self.cnp.text().isdigit() == True and self.findCNP()

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
        if self.service.getLenData() != 0 and self.validateCNP() == True:
            self.linie = self.service.stergereElement(self.cnp.text())
            super().accept()
        else:
            self.showMessage()

    def getLinie(self):
        return self.linie
