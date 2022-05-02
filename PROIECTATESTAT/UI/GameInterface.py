from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QButtonGroup

from Services.GameService import GameService


class GameWindow(QMainWindow):

    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.setWindowTitle('Joc')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('GameWindow')

        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.messageBox = None
        self.intrebari = ("De unde provine oxigenul eliberat prin fotosinteză?",
                          "Cum se numeşte o singură parte din spirala de ADN?",
                          "De unde îşi iau plantele nutrienţii?",
                          'Cum se numesc animalele care mănâncă atât plante cât şi animale?',
                          'Oreionul este o boală cauzată de…?')
        self.raspunsuri = (("Din sol", "Din apa"), ("Cromozom", "Codon"), ("Sol", "Apa"), ("Carnivore", "Omnivore"),
                           ("Virusuri", "Mutatii genetice"))
        self.grupRaspunsuri = QButtonGroup()

        self.initLayout()
        self.grupRaspunsuri.buttonClicked.connect(self.verifRasp)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        stylesheet = '''
            #GameWindow {
                background-image: url(pexels-karolina-grabowska-4210606.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        '''
        self.setStyleSheet(stylesheet)
        self.show()

    def initLayout(self):
        title = QLabel("Intrebari:", self)
        title.setFont(QFont("Times", 30))
        self.layout.addWidget(title, alignment=QtCore.Qt.AlignCenter)
        self.initIntrebari()

    def initIntrebari(self):

        for i in range(0, len(self.intrebari)):
            layoutIntrebare = QVBoxLayout()
            layoutRaspunsuri = QHBoxLayout()

            q = QLabel(self.intrebari[i], self)
            r1 = QRadioButton(self.raspunsuri[i][0], self)
            r2 = QRadioButton(self.raspunsuri[i][1], self)
            r1.setMinimumSize(50, 50)
            r2.setMinimumSize(50, 50)
            r1.setFont(QFont("Times", 15))
            r2.setFont(QFont("Times", 15))
            r1.setChecked(False)
            r2.setChecked(False)
            q.setFont(QFont("Times", 25))

            self.grupRaspunsuri.addButton(r1, 2 * i)
            self.grupRaspunsuri.addButton(r2, 2 * i + 1)
            self.grupRaspunsuri.setExclusive(False)

            layoutIntrebare.addWidget(q, alignment=QtCore.Qt.AlignCenter)

            layoutRaspunsuri.addWidget(r1)
            layoutRaspunsuri.addWidget(r2)
            layoutRaspunsuri.setAlignment(QtCore.Qt.AlignCenter)

            layoutIntrebare.addLayout(layoutRaspunsuri)
            layoutIntrebare.setAlignment(QtCore.Qt.AlignCenter)

            self.layout.addLayout(layoutIntrebare)

    def verifRasp(self, object):
        self.initMessageBox(self.grupRaspunsuri.id(object) // 2 + 1)
        service = GameService(self.grupRaspunsuri.id(object) // 2 + 1, object.text())
        mesaj = ''
        if service.verif_raspuns():
            mesaj = 'Corect!'
        else:
            mesaj = 'Gresit!'

        self.messageBox.setText(mesaj)
        self.messageBox.exec()
        self.messageBox.hide()
        self.grupRaspunsuri.button(self.grupRaspunsuri.id(object)).setChecked(False)
        self.grupRaspunsuri.button(self.grupRaspunsuri.id(object)).unsetCursor()

    def initMessageBox(self, intrebare):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowIcon(QIcon("icons8-information-48.png"))
        self.messageBox.setIcon(QMessageBox.Information)
        self.messageBox.setWindowTitle("Intrebare {}".format(intrebare))
        self.messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.messageBox.setEscapeButton(QMessageBox.Close)
        self.messageBox.setFont(QFont("Times", 10))
        self.messageBox.resize(self.messageBox.sizeHint())
