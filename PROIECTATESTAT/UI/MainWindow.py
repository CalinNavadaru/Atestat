from time import sleep

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton

from UI.GameInterface import GameWindow
from UI.InformationWindow import InformationWindow
from UI.TableWindow import TableWindow


class MainWindow(QMainWindow):  # Opening Window
    def __init__(self):
        super().__init__()
        self.JocWindow = None
        self.InfWindow = None
        self.ListaWindow = None
        self.label = None
        self.setWindowTitle('Proiect Atestat')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('MainWindow')
        self.buttonInf = None
        self.buttonLista = None
        self.buttonJoc = None
        self.buttonModif = None
        self.titlu = None
        self.setTitle()
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

    def setTitle(self):
        self.titlu = QLabel(self)
        self.titlu.setText("Aplicatie Atestat")
        self.titlu.resize(300, 200)
        self.titlu.move(500, -25)
        self.setFont(QFont('Times', 25))
        self.titlu.show()

    def ApasareInf(self):
        self.InfWindow = InformationWindow()

    def ApasareJoc(self):
        self.JocWindow = GameWindow()

    def ApasareLista(self):
        self.ListaWindow = TableWindow()

    def InitButonInf(self):
        self.buttonInf.setToolTip('Buton pentru informatii')
        self.buttonInf.move(510, 600)
        self.buttonInf.setMinimumSize(200, 100)
        self.buttonInf.setFont(QFont('Times', 25))
        self.buttonInf.clicked.connect(self.ApasareInf)

    def InitButonJoc(self):
        self.buttonJoc.setToolTip('Buton pentru joc')
        self.buttonJoc.move(510, 450)
        self.buttonJoc.setMinimumSize(200, 100)
        self.buttonJoc.setFont(QFont('Times', 25))
        self.buttonJoc.clicked.connect(self.ApasareJoc)

    def InitButonModif(self):
        self.buttonModif.setToolTip('Buton pentru informatii')
        self.buttonModif.move(510, 300)
        self.buttonModif.setMinimumSize(200, 100)
        self.buttonModif.setFont(QFont('Times', 15))
        ##self.buttonModif.clicked.connect(self.ApasareInf)

    def InitButonLista(self):
        self.buttonLista.setToolTip('Buton pentru tabel')
        self.buttonLista.move(510, 175)
        self.buttonLista.setMinimumSize(200, 100)
        self.buttonLista.setFont(QFont('Times', 15))
        self.buttonLista.clicked.connect(self.ApasareLista)

    def meniu(self):
        self.buttonInf = QPushButton('Informatii', self)
        self.buttonJoc = QPushButton('Joc', self)
        self.buttonModif = QPushButton('Modificare Tabel', self)
        self.buttonLista = QPushButton("Lista Pacienti", self)
        self.InitButonLista()
        self.InitButonModif()
        self.InitButonJoc()
        self.InitButonInf()
