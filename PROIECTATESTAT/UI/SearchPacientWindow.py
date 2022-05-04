from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox

from UI.MessageWindow import MessageWindow


class SearchPacientWindow(QDialog):

    def __init__(self, service, parent=None):
        super().__init__(parent)
        self.service = service
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        self.setWindowTitle("Căutare Pacient")
        self.setWindowIcon(QIcon("Poze/icons8-search-96.png"))

        self.linie = None
        self.messageBox = None

        self.cnp = QLineEdit(self)
        layout.addRow("CNP", self.cnp)

        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.input)
        buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def showMessage(self):
        self.messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def validateCNP(self):
        return self.cnp.text() != '' and self.cnp.text().isdigit() == True

    def input(self):
        if self.validateCNP():
            self.linie = self.service.SearchPacient(self.cnp.text())
            super().accept()
        else:
            self.showMessage()

    def getLine(self):
        return self.linie
