from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel, QMessageBox

from UI.MessageWindow import MessageWindow


class DeletePacientWindow(QDialog):

    def __init__(self, service, coloane, parent=None):
        super().__init__(parent)
        self.__service = service
        self.__coloane = coloane
        self.__line = None
        self.__messageBox = None
        self.setWindowTitle("Ștergere Pacient")
        self.setWindowIcon(QIcon("Poze/4233089.png"))

        self.__buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.__layout = QFormLayout(self)

        self.__cnp = QLineEdit(self)
        mesaj = QLabel("Introduceți datele pacientului:")
        self.__layout.addWidget(mesaj)
        self.__layout.addRow("CNP Pacient:", self.__cnp)

        self.__layout.addWidget(self.__buttonBox)
        self.__buttonBox.accepted.connect(self.__inputUser)
        self.__buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def __findCNP(self):
        data = self.__service.getData()
        for x in data:
            if x['CNP'] == self.__cnp.text():
                return True

        return False

    def __validateCNP(self):
        return self.__cnp.text() != '' and self.__cnp.text().isdigit() == True and len(self.__cnp.text()) == 13 \
               and self.__findCNP()

    def __showMessage(self):
        self.__messageBox = MessageWindow("Ați introdus o valoare greșită/invalidă!")

    def __inputUser(self):
        if self.__service.getLenData() != 0 and self.__validateCNP() == True:
            self.__line = self.__service.deletePacient(self.__cnp.text().strip())
            super().accept()
        else:
            self.__showMessage()

    def getLine(self):
        return self.__line
