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

        self.__line = None
        self.__messageBox = None

        self.__cnp = QLineEdit(self)
        layout.addRow("CNP", self.__cnp)

        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.__input)
        buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def __showMessage(self):
        self.__messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def __validateCNP(self):
        return self.__cnp.text() != '' and self.__cnp.text().isdigit() == True and len(self.__cnp.text()) == 13

    def __input(self):
        if self.__validateCNP():
            self.__line = self.service.SearchPacient(self.__cnp.text())
            super().accept()
        else:
            self.__showMessage()

    def getLine(self):
        return self.__line
