from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QPushButton, QHBoxLayout, \
    QButtonGroup

from Services.TableService import TableService
from UI.AddPacientWindow import AddPacientWindow
from UI.SearchPacientWindow import SearchPacientWindow
from UI.ModifWindow import ModifWindow
from UI.DeletePacientWindow import DeletePacientWindow

coloane = ('Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice')
buttonNames = ("Adauga", "Modificare", "Sterge", "Cauta in tabel")


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Lista Pacienti")

        self.table = QTableWidget()
        self.layoutButtons = QHBoxLayout()
        self.service = TableService()
        self.layout = QVBoxLayout()
        self.buttonGroup = QButtonGroup()

        self.buttons = []

        self.butonAdaugare = None
        self.butonCautare = None
        self.butonModif = None
        self.butonStergere = None

        self.initButtons()
        self.createTable()
        self.fillTable()

        self.buttonGroup.buttonClicked.connect(self.handler)

        self.layoutButtons.setAlignment(QtCore.Qt.AlignLeft)
        self.layoutButtons.setSpacing(25)

        self.layout.addLayout(self.layoutButtons)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.show()

    def initButtons(self):
        k = 1
        for btnName in buttonNames:
            button = QPushButton(btnName, self)
            button.setFont(QFont("Times", 20))
            button.setMaximumSize(250, 100)
            self.buttonGroup.addButton(button, k)
            self.layoutButtons.addWidget(button, 1)
            k += 1

    def createTable(self):
        self.table.setRowCount(25)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(coloane)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def fillTable(self):

        date = self.service.initTable()
        for i in range(0, len(date)):
            k = 1
            for x in date[i].values():
                self.table.setItem(i, k - 1, QTableWidgetItem(x))
                k += 1

    def handler(self, button):
        functions = {
            "1": self.pressedAdd,
            "2": self.pressedUpdate,
            "3": self.pressedDelete,
            "4": self.pressedSearch
        }
        functions[str(self.buttonGroup.id(button))]()

    def pressedDelete(self):
        deleteWindow = DeletePacientWindow(self.service, coloane)
        if self.service.getLenData() != 0:
            self.table.hideRow(deleteWindow.getLinie())
            self.fillTable()

    def pressedAdd(self):
        adaugareWindow = AddPacientWindow(self.service, coloane)
        self.fillTable()

    def pressedUpdate(self):
        modifWindow = ModifWindow(self.service, coloane)
        self.fillTable()

    def pressedSearch(self):
        indexWindow = SearchPacientWindow(self.service, self)
        linie = indexWindow.getLine()
        print(linie)
        if linie is not None:
            self.table.selectRow(linie - 1)
