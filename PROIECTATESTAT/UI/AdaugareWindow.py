from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit


class AdaugareWindow(QDialog):

    def __init__(self, service, coloane : list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adaugare Pacient")
        self.coloane = coloane
        self.campuri = []
        self.userInput = []
        self.setWindowIcon(QIcon("add-user.png"))
        self.service = service
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout = QFormLayout(self)
        self.initCampuri()
        self.layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.inputUser)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def inputUser(self):
        self.userInput = [x.text() for x in self.campuri]
        self.service.adaugarePacient(self.coloane, self.userInput)
        super().accept()

    def initCampuri(self):
        for x in self.coloane:
            inputCamp = QLineEdit(self)
            self.layout.addRow(x, inputCamp)
            self.campuri.append(inputCamp)
