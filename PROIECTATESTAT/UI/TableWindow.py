from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QPushButton, QHBoxLayout, \
    QDialog, QDialogButtonBox

from Services.TableService import TableService
from UI.CautareWindow import CautareWindow

coloane = ['Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice']


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        self.table = QTableWidget()
        self.layoutButon = QHBoxLayout()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Lista Pacienti")
        self.butonModif = None
        self.butonCautare = None
        self.initButonModif()
        self.initButonCautare()
        self.createTable()
        self.fillTable()

        self.layoutButon.setAlignment(QtCore.Qt.AlignLeft)
        self.layoutButon.setSpacing(25)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.layoutButon)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.show()

    def fillTable(self):
        service = TableService()
        date = service.initTable()
        for i in range(0, len(date)):
            k = 1
            for x in date[i].values():
                self.table.setItem(i, k - 1, QTableWidgetItem(x))
                k += 1

    def initButonModif(self):
        self.butonModif = QPushButton()
        self.butonModif.setText("Modifica tabel")
        self.butonModif.setFont(QFont("Times", 20))
        self.butonModif.setMaximumSize(200, 100)
        self.layoutButon.addWidget(self.butonModif, 1)

    def apasareCautare(self):
        indexWindow = CautareWindow(coloane, self)

    def initButonCautare(self):
        self.butonCautare = QPushButton()
        self.butonCautare.setText("Cauta in tabel")
        self.butonCautare.setFont(QFont("Times", 20))
        self.butonCautare.setMaximumSize(200, 100)
        self.butonCautare.clicked.connect(self.apasareCautare)
        self.layoutButon.addWidget(self.butonCautare, 2)

    def createTable(self):
        self.table.setRowCount(25)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(coloane)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
