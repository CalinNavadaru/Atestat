from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QMessageBox


class SearchPacientWindow(QDialog):

    def __init__(self, service, parent=None):
        super().__init__(parent)
        self.service = service
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        self.setWindowTitle("Cautare")
        self.setWindowIcon(QIcon("icons8-search-96.png"))

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

    def input(self):
        if self.cnp.text() != '' and self.cnp.text().isdigit() == True:
            self.linie = self.service.SearchPacient(self.cnp.text())
            super().accept()
        else:
            self.showMessage()

    def getLine(self):
        return self.linie
