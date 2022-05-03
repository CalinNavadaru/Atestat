from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit, QLabel

from Services import TableService


class DeletePacientWindow(QDialog):

    def __init__(self, service, coloane, parent=None):
        super().__init__(parent)
        self.service = service
        self.coloane = coloane
        self.linie = None
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

    def inputUser(self):
        if self.service.getLenData() != 0:
            self.linie = self.service.stergereElement(self.cnp.text())
        super().accept()

    def getLinie(self):
        return self.linie
