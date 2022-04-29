from PyQt5 import QtCore, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QApplication, \
    QWidget, QTableView, QPushButton

coloane = ['Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice']


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Lista Pacienti")
        self.butonModif = None
        self.initButonModif()
        self.createTable()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.butonModif)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        # Show window
        self.show()

    def initButonModif(self):
        self.butonModif = QPushButton()
        self.butonModif.setText("Modifica tabel")
        self.butonModif.setFont(QFont("Times", 20))
        self.butonModif.setMaximumSize(200, 100)

    def createTable(self):
        self.table.setRowCount(25)
        self.table.setColumnCount(7)
        self.table.setItem(2, 2, QTableWidgetItem("Calin"))
        self.table.setItem(3, 3, QTableWidgetItem("Calin"))
        self.table.setHorizontalHeaderLabels(coloane)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
