from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QPushButton, QHBoxLayout

from Services.TableService import TableService
from UI.AdaugareWindow import AdaugareWindow
from UI.CautareWindow import CautareWindow

coloane = ['Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice']


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        self.table = QTableWidget()
        self.layoutButon = QHBoxLayout()
        self.service = TableService()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Lista Pacienti")
        self.butonAdaugare = None
        self.butonCautare = None
        self.initButonAdaugare()
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

        date = self.service.initTable()
        for i in range(0, len(date)):
            k = 1
            for x in date[i].values():
                self.table.setItem(i, k - 1, QTableWidgetItem(x))
                k += 1

    def apasareAdaugare(self):
        adaugareWindow = AdaugareWindow(self.service, coloane)
        self.fillTable()

    def initButonAdaugare(self):
        self.butonAdaugare = QPushButton()
        self.butonAdaugare.setText("Adauga")
        self.butonAdaugare.setFont(QFont("Times", 20))
        self.butonAdaugare.setMaximumSize(200, 100)
        self.butonAdaugare.clicked.connect(self.apasareAdaugare)
        self.layoutButon.addWidget(self.butonAdaugare, 1)

    def apasareCautare(self):
        indexWindow = CautareWindow(coloane, self.service, self)
        linie = indexWindow.getLine()
        print(linie)
        if linie is not None:
            self.table.selectRow(linie - 1)

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
