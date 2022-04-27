from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QButtonGroup, QGroupBox

from Services.GameService import GameService


class GameWindow(QMainWindow):
    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)
        self.layout = QVBoxLayout()
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
        # self.Intrebare2()
        # self.Intrebare3()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        stylesheet = '''
            #GameWindow {
                background-image: url(pexels-chokniti-khongchum-2280549.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        '''
        self.setStyleSheet(stylesheet)
        self.show()

    def verif_rasp_1(self, rasp):
        raspuns = QMessageBox(self)
        raspuns.setIcon(QMessageBox.Information)
        service = GameService(1, rasp)
        mesaj = ''
        if service.verif_raspuns():
            mesaj = 'Corect!'
        else:
            mesaj = 'Gresit!'
        raspuns.setText(mesaj)
        raspuns.exec()
        raspuns.hide()
        self.hide()

    def initLayoutIntrebare(self, cerinta, buton1, buton2):
        grupRadio = QGroupBox()
        layout_radio = QHBoxLayout()
        layout_radio.addWidget(buton1)
        layout_radio.addWidget(buton2)
        layout_radio.addStretch(1)
        layout_radio.setAlignment(QtCore.Qt.AlignCenter)
        grupRadio.setLayout(layout_radio)
        grupRadio.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(cerinta)
        self.layout.addWidget(grupRadio)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

    def run(self):
        while True:
            if self.r1.isChecked():
                self.verif_rasp_1("Din sol")
            elif self.r2.isChecked():
                self.verif_rasp_1("Din apa")

    def Intrebare1(self):
        self.q1 = QLabel("De unde provine oxigenul eliberat prin fotosinteză?")
        self.q1.setFont(QFont("Times", 25))
        self.r1 = QRadioButton("Din sol", self)
        self.r2 = QRadioButton("Din apă", self)
        self.r1.setCheckable(True)
        self.r2.setCheckable(True)
        self.r1.setChecked(False)
        self.r2.setChecked(False)
        print(self.r1.isChecked())
        print(self.r2.isChecked())
        self.initLayoutIntrebare(self.q1, self.r1, self.r2)
        self.r1.clicked.connect(self.run)
        self.r2.clicked.connect(self.run)

    def Intrebare2(self):
        self.q2 = QLabel("Cum se numeşte o singură parte din spirala de ADN?")
        self.q2.setFont(QFont("Times", 25))
        self.r3 = QRadioButton("Cromozom")
        self.r4 = QRadioButton("Codon")
        self.initLayoutIntrebare(self.q2, self.r3, self.r4)

    def Intrebare3(self):
        self.q3 = QLabel("De unde îşi iau plantele nutrienţii?")
        self.q3.setFont(QFont("Times", 25))
        self.r5 = QRadioButton("Sol", self)
        self.r6 = QRadioButton("Apa")
        self.initLayoutIntrebare(self.q3, self.r5, self.r6)
