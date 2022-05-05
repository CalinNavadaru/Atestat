from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel, QMessageBox

from UI.MessageWindow import MessageWindow


class DeletePacientWindow(QDialog):

    def __init__(self, service, coloane, parent=None):
        super().__init__(parent)
        self.service = service
        self.coloane = coloane
        self.linie = None
        self.messageBox = None
        self.setWindowTitle("Ștergere Pacient")
        self.setWindowIcon(QIcon("Poze/4233089.png"))

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)

        self.cnp = QLineEdit(self)
        mesaj = QLabel("Introduceți datele pacientului:")
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
        return self.cnp.text() != '' and self.cnp.text().isdigit() == True and len(self.cnp.text()) == 13\
               and self.findCNP()

    def showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def inputUser(self):
        if self.service.getLenData() != 0 and self.validateCNP() == True:
            self.linie = self.service.deletePacient(self.cnp.text().strip())
            super().accept()
        else:
            self.showMessage()

    def getLinie(self):
        return self.linie
