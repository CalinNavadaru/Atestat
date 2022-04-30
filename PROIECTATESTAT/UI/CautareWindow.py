from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit


class CautareWindow(QDialog):

    def __init__(self, coloane, service, parent=None):
        super().__init__(parent)
        self.service = service
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        self.setWindowTitle("Cautare")
        self.setWindowIcon(QIcon("icons8-search-96.png"))

        self.linie = None

        self.cnp = QLineEdit(self)
        layout.addRow("CNP", self.cnp)

        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.input)
        buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def input(self):
        self.linie = self.service.CautareElement(self.cnp.text())
        super().accept()
