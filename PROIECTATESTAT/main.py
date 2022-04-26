import sys

from PyQt5.QtWidgets import QApplication

from UI.InformationWindow import InformationWindow
from UI.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
