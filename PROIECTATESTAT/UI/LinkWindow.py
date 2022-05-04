from PyQt5 import Qt, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMainWindow


class LinkWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Link-uri utile")
        self.setWindowIcon(QIcon("Poze/icons8-information-48.png"))
        self.setFixedSize(800, 600)
        self.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.setObjectName('LinkWindow')
        self.linkuri = {
            "Case de asigurări": 'https://www.romedic.ro/case-de-asigurari-de-sanatate-0G1224',
            "Medicină internă": 'https://www.medicina-interna.ro',
            "Casa mediciilor din România": 'https://www.cmr.ro',
            "Portaluri Medicale": 'https://www.romedic.ro/portaluri-medicale-0G27003',
            "Verificare Asigurat": 'http://cas.cnas.ro/page/verificare-asigurat.html'
        }
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.title = None
        self.styleSheetTitle = None
        self.styleSheetBackground = None

        self.initStyleSheets()
        self.setupUI()

        self.setLayout(self.layout)
        self.setStyleSheet(self.styleSheetBackground)
        self.show()

    def setupLinks(self):
        for key, value in self.linkuri.items():
            label = QLabel('<a href={}>{}</a>'.format(value, key))
            label.setFont(QFont("Times", 25))
            label.setOpenExternalLinks(True)
            self.layout.addWidget(label, alignment=QtCore.Qt.AlignCenter)

    def initStyleSheets(self):
        self.styleSheetBackground = '''
                            #LinkWindow {
                                background-image: url(Poze/pexels-kindel-media-8325716.jpg);
                                background-repeat: no-repeat;
                                background-position: center;
                            }
                        '''

        self.styleSheetTitle = '''
                        #Title {
                            color : black;
                        }
                        '''

    def setupUI(self):
        layout = QHBoxLayout()
        self.title = QLabel("Link-uri utile: ")
        self.title.setObjectName("Title")
        self.title.setFont(QFont("Times", 25))
        self.title.setStyleSheet(self.styleSheetTitle)
        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignLeft)

        self.setupLinks()
