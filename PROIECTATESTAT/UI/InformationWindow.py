from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget


class InformationWindow(QMainWindow):

    def __init__(self, parent=None):
        super(InformationWindow, self).__init__(parent)

        self.setWindowTitle('Informatii')
        self.setFixedSize(600, 400)
        self.setObjectName('InformationWindow')
        self.setWindowIcon(QIcon("Poze/icons8-information-48.png"))

        self.message = 'Aplicație realizată de Năvădaru Călin din clasa a-12-a C de ' \
                     'la Colegiul Național Gr. Moisil Brașov ' \
                        'în limbajul Python și cu ajutorul bazei de date MongoDB.' \
                       ' \n' \
                     'Email: navadarucalin@yahoo.com\n' \
                     r'Versiune: 1.0'

        self.text = None
        self.title = None
        self.image = None

        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.printMessage()

        stylesheet = '''
    #InformationWindow {
        background-image: url(Poze/pexels-kindel-media-8325716.jpg);
        background-repeat: no-repeat;
        background-position: center;
    }
'''
        self.setStyleSheet(stylesheet)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.show()

    def printMessage(self):
        self.title = QLabel("Informații", self)
        self.title.setFont(QFont("Times", 20))
        self.layout.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)

        self.text = QLabel(self)
        self.text.setFont(QFont("Times", 15))
        self.text.setWordWrap(True)
        self.text.setText(self.message)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.text, alignment=QtCore.Qt.AlignCenter)

        self.image = QLabel()
        self.image.setPixmap(QPixmap("Poze/index.png"))
        self.layout.addWidget(self.image, alignment=QtCore.Qt.AlignCenter)

        self.layout.setSpacing(20)
