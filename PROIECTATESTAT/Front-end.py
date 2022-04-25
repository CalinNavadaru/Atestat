import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton, QAction


class App(QMainWindow):  # Opening Window
    def __init__(self):
        super().__init__()
        self.label = None
        self.setWindowTitle('Proiect Atestat')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('MainWindow')
        self.buttonInf = None
        self.buttonLista = None
        self.buttonJoc = None
        self.buttonModif = None

        stylesheet = '''
    #MainWindow {
        background-image: url(pexels-chokniti-khongchum-2280549.jpg);
        background-repeat: no-repeat;
        background-position: center;
    }
'''
        self.setStyleSheet(stylesheet)
        self.meniu()
        self.show()

    def InitButonInf(self):
        self.buttonInf.setToolTip('Buton pentru informatii')
        self.buttonInf.move(700, 500)
        self.buttonInf.setMinimumSize(250, 150)
        self.buttonInf.setFont(QFont('Times', 35))
        #self.buttonInf.clicked.connect(self.ApasareInf)

    def meniu(self):
        self.buttonInf = QPushButton('Informatii', self)
        #self.buttonLista = QPushButton('Lista pacienti', self)
        #self.buttonJoc = QPushButton('Joc', self)
        #self.buttonModif = QPushButton('Modificare Date', self)
        self.InitButonInf()

    def apasare(self):
        print("sada")
        self.label = QLabel("sada")
        self.label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
