from PyQt5 import QtCore, Qt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

from UI.GameInterface import GameWindow
from UI.InformationWindow import InformationWindow
from UI.LinkWindow import LinkWindow
from UI.TableWindow import TableWindow

buttonNames = ('Tabel Pacienți', 'Joc', 'Informații', 'Linkuri Utile')
buttonToolTips = ('Buton pentru tabel', 'Buton pentru joc', 'Buton pentru informații', 'Buton pentru link-uri utile')


class MainWindow(QMainWindow):  # Opening Window

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Proiect Atestat')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('MainWindow')

        self.func = {
            "0": self.__PressedTableBtn,
            "1": self.__PressedGameBtn,
            "2": self.__PressedInfoBtn,
            "3": self.__PressedLinkBtn
        }
        self.title = None
        self.styleSheetBtn = None
        self.styleSheetBackground = None
        self.styleSheetTitle = None
        self.GameWindow = None
        self.InfWindow = None
        self.TableWindow = None
        self.LinkWindow = None
        self.buttons = []

        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.__initStyleSheets()
        self.__setTitle()
        self.__initButons()

        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setSpacing(25)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.setStyleSheet(self.styleSheetBackground)
        self.show()

    def __initStyleSheets(self):
        self.styleSheetBackground = '''
                    #MainWindow {
                        background-image: url(Poze/pexels-chokniti-khongchum-2280549.jpg);
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

    def __PressedInfoBtn(self):
        self.InfWindow = InformationWindow()

    def __PressedGameBtn(self):
        self.GameWindow = GameWindow()

    def __PressedTableBtn(self):
        self.TableWindow = TableWindow()

    def __PressedLinkBtn(self):
        self.LinkWindow = LinkWindow()

    def __setTitle(self):
        self.title = QLabel()
        self.title.setText("Aplicație Gestiune cabinet medical")
        self.title.setMinimumSize(250, 200)
        self.title.setFont(QFont('Times', 25))
        self.title.setObjectName("Title")
        self.title.setStyleSheet(self.styleSheetTitle)
        self.layout.addWidget(self.title, alignment=Qt.AlignCenter)

    def __initButons(self):
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

        upperLayout = QHBoxLayout(self)
        upperLayout.addWidget(self.buttons[0], alignment=QtCore.Qt.AlignCenter)
        upperLayout.addWidget(self.buttons[1], alignment=QtCore.Qt.AlignCenter)
        upperLayout.setAlignment(QtCore.Qt.AlignCenter)
        upperLayout.addSpacing(50)

        lowerLayout = QHBoxLayout(self)
        lowerLayout.addWidget(self.buttons[2], alignment=QtCore.Qt.AlignCenter)
        lowerLayout.addWidget(self.buttons[3], alignment=QtCore.Qt.AlignCenter)
        lowerLayout.setAlignment(QtCore.Qt.AlignCenter)
        lowerLayout.addSpacing(50)

        layoutButtons.addLayout(upperLayout)
        layoutButtons.addLayout(lowerLayout)
        layoutButtons.setAlignment(QtCore.Qt.AlignCenter)
        layoutButtons.setSpacing(50)

        self.layout.addLayout(layoutButtons)
