from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox, \
    QButtonGroup

from Services.GameService import GameService


class GameWindow(QMainWindow):

    def __init__(self, parent=None):
        super(GameWindow, self).__init__(parent)

        self.setWindowTitle('Joc')
        self.setWindowIcon(QIcon("Poze/football_13302.png"))
        self.setMinimumSize(1280, 720)
        self.setMaximumSize(1280, 720)
        self.setObjectName('GameWindow')

        self.layout = QVBoxLayout()
        self.widget = QWidget()

        self.messageBox = None
        self.questions = ("De unde provine oxigenul eliberat prin fotosinteză?",
                          "Cum se numeşte o singură parte din spirala de ADN?",
                          "De unde îşi iau plantele nutrienţii?",
                          'Cum se numesc animalele care mănâncă atât plante cât şi animale?',
                          'Oreionul este o boală cauzată de…?')
        self.answers = (("Din sol", "Din apa"), ("Cromozom", "Codon"), ("Sol", "Apă"), ("Carnivore", "Omnivore"),
                           ("Virusuri", "Mutații genetice"))
        self.groupAnswers = QButtonGroup()

        self.initLayout()
        self.groupAnswers.buttonClicked.connect(self.validateAnswer)
        
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        stylesheet = '''
            #GameWindow {
                background-image: url(Poze/pexels-karolina-grabowska-4210606.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        '''
        self.setStyleSheet(stylesheet)
        self.show()

    def initLayout(self):
        title = QLabel("Intrebări", self)
        title.setFont(QFont("Times", 30))
        self.layout.addWidget(title, alignment=QtCore.Qt.AlignCenter)
        self.initIntrebari()

    def initIntrebari(self):

        for i in range(0, len(self.questions)):
            layoutQuestion = QVBoxLayout()
            layoutAnswer = QHBoxLayout()

            q = QLabel(self.questions[i], self)
            r1 = QRadioButton(self.answers[i][0], self)
            r2 = QRadioButton(self.answers[i][1], self)
            r1.setMinimumSize(50, 50)
            r2.setMinimumSize(50, 50)
            r1.setFont(QFont("Times", 15))
            r2.setFont(QFont("Times", 15))
            r1.setChecked(False)
            r2.setChecked(False)
            q.setFont(QFont("Times", 25))

            self.groupAnswers.addButton(r1, 2 * i)
            self.groupAnswers.addButton(r2, 2 * i + 1)
            self.groupAnswers.setExclusive(False)

            layoutQuestion.addWidget(q, alignment=QtCore.Qt.AlignCenter)

            layoutAnswer.addWidget(r1)
            layoutAnswer.addWidget(r2)
            layoutAnswer.setAlignment(QtCore.Qt.AlignCenter)

            layoutQuestion.addLayout(layoutAnswer)
            layoutQuestion.setAlignment(QtCore.Qt.AlignCenter)

            self.layout.addLayout(layoutQuestion)

    def validateAnswer(self, object):
        self.initMessageBox(self.groupAnswers.id(object) // 2 + 1)
        service = GameService(self.groupAnswers.id(object) // 2 + 1, object.text())
        message = ''
        if service.verif_raspuns():
            message = 'Corect!'
        else:
            message = 'Greșit!'

        self.messageBox.setText(message)
        self.messageBox.exec()
        self.messageBox.hide()
        self.groupAnswers.button(self.groupAnswers.id(object)).setChecked(False)
        self.groupAnswers.button(self.groupAnswers.id(object)).unsetCursor()

    def initMessageBox(self, intrebare):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowIcon(QIcon("Poze/icons8-information-48.png"))
        self.messageBox.setIcon(QMessageBox.Information)
        self.messageBox.setWindowTitle("Intrebare {}".format(intrebare))
        self.messageBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
        self.messageBox.setEscapeButton(QMessageBox.Close)
        self.messageBox.setFont(QFont("Times", 10))
        self.messageBox.resize(self.messageBox.sizeHint())
