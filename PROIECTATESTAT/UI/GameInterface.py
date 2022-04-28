from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QButtonGroup, QGroupBox

from Services.GameService import GameService


# TODO Mai multe Intrebari
# TODO Restructurare
# TODO Interfata

class GameWindow(QMainWindow):

    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.messagebox = None
        self.widget = QWidget()
        self.q1 = None
        self.q2 = None
        self.q3 = None
        self.r1 = None
        self.r2 = None
        self.r3 = None
        self.r4 = None
        self.r5 = None
        self.r6 = None
        self.setWindowTitle('Joc')
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('GameWindow')
        self.Intrebare1()
        self.Intrebare2()
        self.Intrebare3()
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

    def initMessageBox(self, intrebare):
        self.messagebox = QMessageBox(self)
        self.messagebox.setIcon(QMessageBox.Information)
        self.messagebox.setWindowTitle("Intrebare {}".format(intrebare))
        self.messagebox.setFont(QFont("Times", 15))
        self.messagebox.resize(500, 500)

    def verif_rasp(self, intrebare, rasp, r1: QRadioButton):
        self.initMessageBox(intrebare)
        service = GameService(intrebare, rasp)
        mesaj = ''
        if service.verif_raspuns():
            mesaj = 'Corect!'
        else:
            mesaj = 'Gresit!'

        # r1.clicked.disconnect(self.run)
        r1.setChecked(False)
        r1.unsetCursor()
        self.messagebox.setText(mesaj)
        self.messagebox.exec()
        self.messagebox.hide()
        return False

    def initLayoutIntrebare(self, cerinta, buton1, buton2):
        grupRadio = QButtonGroup()
        layoutIntrebare = QVBoxLayout()
        layoutRaspunsuri = QHBoxLayout()

        grupRadio.setExclusive(False)
        grupRadio.addButton(buton1)
        grupRadio.addButton(buton2)

        layoutRaspunsuri.addWidget(buton1)
        layoutRaspunsuri.addWidget(buton2)
        layoutRaspunsuri.setAlignment(QtCore.Qt.AlignCenter)

        layoutIntrebare.addWidget(cerinta)
        layoutIntrebare.addLayout(layoutRaspunsuri)
        layoutIntrebare.setAlignment(QtCore.Qt.AlignCenter)
        layoutIntrebare.setSpacing(15)

        self.layout.addLayout(layoutIntrebare)
        self.layout.setAlignment(QtCore.Qt.AlignVCenter)
        self.layout.setSpacing(30)

    def run(self):
        if self.r1.isChecked():
            self.verif_rasp(1, "Din sol", self.r1)
        elif self.r2.isChecked():
            self.verif_rasp(1, "Din apa", self.r2)

        elif self.r3.isChecked():
            self.verif_rasp(2, "Cromozom", self.r3)

        elif self.r4.isChecked():
            self.verif_rasp(2, "Codon", self.r4)

        elif self.r5.isChecked():
            self.verif_rasp(3, "Sol", self.r5)

        elif self.r6.isChecked():
            self.verif_rasp(3, "Apa", self.r6)

    def Intrebare1(self):
        self.q1 = QLabel("De unde provine oxigenul eliberat prin fotosinteză?")
        self.q1.setFont(QFont("Times", 25))
        self.r1 = QRadioButton("Din sol", self)
        self.r2 = QRadioButton("Din apă", self)
        self.r1.setChecked(False)
        self.r2.setChecked(False)
        self.initLayoutIntrebare(self.q1, self.r1, self.r2)
        self.r1.clicked.connect(self.run)
        self.r2.clicked.connect(self.run)

    def Intrebare2(self):
        self.q2 = QLabel("Cum se numeşte o singură parte din spirala de ADN?")
        self.q2.setFont(QFont("Times", 25))
        self.r3 = QRadioButton("Cromozom")
        self.r4 = QRadioButton("Codon")
        self.r3.setChecked(False)
        self.r4.setChecked(False)
        self.initLayoutIntrebare(self.q2, self.r3, self.r4)
        self.r3.clicked.connect(self.run)
        self.r4.clicked.connect(self.run)

    def Intrebare3(self):
        self.q3 = QLabel("De unde îşi iau plantele nutrienţii?")
        self.q3.setFont(QFont("Times", 25))
        self.r5 = QRadioButton("Sol", self)
        self.r6 = QRadioButton("Apa")
        self.r5.setChecked(False)
        self.r6.setChecked(False)
        self.initLayoutIntrebare(self.q3, self.r5, self.r6)
        self.r5.clicked.connect(self.run)
        self.r6.clicked.connect(self.run)
