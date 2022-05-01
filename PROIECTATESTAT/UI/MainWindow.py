from time import sleep

from PyQt5 import QtCore, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

from UI.GameInterface import GameWindow
from UI.InformationWindow import InformationWindow
from UI.LinkWindow import LinkWindow
from UI.TableWindow import TableWindow

buttonNames = ('Tabel Pacienti', 'Joc', 'Informatii', 'Linkuri Utile')
buttonToolTips = ('Buton pentru tabel', 'Buton pentru joc', 'Buton pentru informatii', 'Buton pentru link-uri utile')


class MainWindow(QMainWindow):  # Opening Window
    styleSheetBackground: str

    def __init__(self):
        super().__init__()
        self.func = {
            "0": self.PressedTableBtn,
            "1": self.PressedGameBtn,
            "2": self.PressedInfoBtn,
            "3": self.PressedLinkBtn
        }
        self.styleSheetBtn = None
        self.styleSheetBackground = None
        self.styleSheetTitle = None
        self.initStyleSheets()
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.JocWindow = None
        self.InfWindow = None
        self.ListaWindow = None
        self.LinkWindow = None
        self.buttons = []
        self.setWindowTitle('Proiect Atestat')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('MainWindow')
        self.title = None
        self.setTitle()
        self.initButons()
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setSpacing(25)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.setStyleSheet(self.styleSheetBackground)
        self.show()

    def initStyleSheets(self):
        self.styleSheetBackground = '''
                    #MainWindow {
                        background-image: url(pexels-chokniti-khongchum-2280549.jpg);
                        background-repeat: no-repeat;
                        background-position: center;
                    }
                '''
        self.styleSheetBtn = '''
                        #Btn {
                        background-color: #00b197;
                        border-style: outset;
                        border-width: 2px;
                        border-radius: 15px;
                        border-color: black;
                        padding: 4px;
                        }
                        '''
        self.styleSheetTitle = '''
        #Title {
            color : black;
        }
        '''

    def setTitle(self):
        self.title = QLabel()
        self.title.setText("Aplicatie Atestat")
        self.title.setFixedSize(250, 200)
        self.title.setFont(QFont('Times', 25))
        self.title.setObjectName("Title")
        self.title.setStyleSheet(self.styleSheetTitle)
        self.layout.addWidget(self.title, alignment=Qt.AlignCenter)

    def PressedInfoBtn(self):
        self.InfWindow = InformationWindow()

    def PressedGameBtn(self):
        self.JocWindow = GameWindow()

    def PressedTableBtn(self):
        self.ListaWindow = TableWindow()

    def PressedLinkBtn(self):
        self.LinkWindow = LinkWindow()

    def initButons(self):
        for i in range(len(buttonNames)):
            self.buttons.append(QPushButton(buttonNames[i]))
            q = QPushButton()
            self.buttons[i].setToolTip(buttonToolTips[i])
            self.buttons[i].setFixedSize(325, 150)
            self.buttons[i].setFont(QFont('Times', 15))
            self.buttons[i].setObjectName("Btn")
            self.buttons[i].setStyleSheet(self.styleSheetBtn)
            self.buttons[i].clicked.connect(self.func[str(i)])

        layoutButtons = QVBoxLayout()

        upperLayout = QHBoxLayout()
        upperLayout.addWidget(self.buttons[0])
        upperLayout.addWidget(self.buttons[1])
        upperLayout.addSpacing(50)
        upperLayout.setAlignment(QtCore.Qt.AlignCenter)

        lowerLayout = QHBoxLayout()
        lowerLayout.addWidget(self.buttons[2])
        lowerLayout.addWidget(self.buttons[3])
        lowerLayout.addSpacing(50)
        lowerLayout.setAlignment(QtCore.Qt.AlignCenter)

        layoutButtons.addLayout(upperLayout)
        layoutButtons.addLayout(lowerLayout)
        layoutButtons.setSpacing(100)

        layoutButtons.setAlignment(QtCore.Qt.AlignVCenter)

        self.layout.addLayout(layoutButtons)


