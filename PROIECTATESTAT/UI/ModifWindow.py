from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel


class ModifWindow(QDialog):

    def __init__(self, service, coloane : list, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Modificare Pacient")
        self.coloane = coloane
        self.campuri = []
        self.userInput = []
        self.index = None
        self.setWindowIcon(QIcon("icons8-user-24.png"))
        self.service = service
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.layout = QFormLayout(self)
        self.initLayout()
        self.layout.addWidget(self.buttonBox)
        self.buttonBox.accepted.connect(self.inputUser)
        self.buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.exec()

    def inputUser(self):
        newPacient = [x.text() for x in self.campuri]
        index = int(self.index.text())
        self.service.modificarePacient(self.coloane, index, newPacient)
        super().accept()

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
