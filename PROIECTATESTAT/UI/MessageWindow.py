from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMessageBox


class MessageWindow(QMessageBox):

    def __init__(self, text):
        super().__init__()

        self.setWindowIcon(QIcon("Poze/icons8-information-48.png"))
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Eroare!")
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.setEscapeButton(QMessageBox.Close)
        self.setFont(QFont("Times", 10))
        self.resize(self.sizeHint())
        self.setText(text)
        self.exec()