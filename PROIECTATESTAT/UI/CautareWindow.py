from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QFormLayout, QLineEdit


class CautareWindow(QDialog):

    def __init__(self, coloane, parent=None):
        super().__init__(parent)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        layout = QFormLayout(self)
        self.setWindowTitle("Cautare")
        self.setWindowIcon(QIcon("icons8-search-96.png"))

        self.cnp = QLineEdit(self)
        layout.addRow("CNP", self.cnp)

        layout.addWidget(buttonBox)
        buttonBox.accepted.connect(self.ok)
        buttonBox.rejected.connect(self.reject)

        self.setModal(True)

        self.show()

    def ok(self):
        pass
