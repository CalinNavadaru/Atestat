from PyQt5 import Qt, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLabel, QGridLayout, QWidget


class InformationWindow(QMainWindow):
    def __init__(self, parent=None):
        super(InformationWindow, self).__init__(parent)
        self.label = None
        self.setWindowTitle('Informatii')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('InformationWindow')
        self.afiseazaMesaj()
        self.mesaj = None
        stylesheet = '''
    #InformationWindow {
        background-image: url(pexels-chokniti-khongchum-2280549.jpg);
        background-repeat: no-repeat;
        background-position: center;
    }
'''
        self.setStyleSheet(stylesheet)

    def afiseazaMesaj(self):
        self.mesaj = QLabel(self)
        self.mesaj.setText("Aplicatie realizata de Calin Navadaru.\n")
        self.mesaj.text()
        self.mesaj.setText("Aplicatie realizata de Calin Navadaru.\nIn clasa a 12-C de la Colegiul GR. Moisil Brasov\nVersiunea 1.0")
        self.mesaj.setObjectName("Mesaj")
        stylesheet = '''
            #Mesaj {
            
            color: black;
            }
        '''
        self.mesaj.setStyleSheet(stylesheet)
        self.mesaj.resize(800, 800)
        self.mesaj.move(300, 150)
        self.mesaj.setAlignment(QtCore.Qt.AlignLeft)
        self.mesaj.setFont(QFont('Times', 40))
        self.mesaj.setWordWrap(True)
        self.mesaj.show()