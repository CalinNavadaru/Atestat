from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget


class InformationWindow(QMainWindow):

    def __init__(self, parent=None):
        super(InformationWindow, self).__init__(parent)
        self.setWindowTitle('Informatii')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('InformationWindow')

        self.mesaj = 'Aplicatie realizata in Python si Mongodb\nde Năvădaru Călin din clasa a 12-C\nde ' \
                     'la Colegiul National Gr. Moisil Brasov\n' \
                     'Email: navadarucalin@yahoo.com\n' \
                     r'Versiune 1.0'

        self.text = None
        self.text2 = None

        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.afiseazaMesaj()

        stylesheet = '''
    #InformationWindow {
        background-image: url(pexels-chokniti-khongchum-2280549.jpg);
        background-repeat: no-repeat;
        background-position: center;
    }
'''
        self.setStyleSheet(stylesheet)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.show()

    def afiseazaMesaj(self):
        self.text = QLabel(self)
        self.text.setFont(QFont("Times", 40))
        self.text.setWordWrap(True)
        self.text.setMinimumSize(900, 400)
        self.text.setText(self.mesaj)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.text, alignment=QtCore.Qt.AlignCenter)

        self.layout.setSpacing(10)
