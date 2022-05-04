from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QPushButton, QHBoxLayout, \
    QButtonGroup, QMessageBox

from Services.TableService import TableService
from UI.AddPacientWindow import AddPacientWindow
from UI.MessageWindow import MessageWindow
from UI.SearchPacientWindow import SearchPacientWindow
from UI.UpdatePacient import UpdateWindow
from UI.DeletePacientWindow import DeletePacientWindow

coloane = ('Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice')
buttonNames = ("Adaugă", "Modificare", "Șterge", "Caută în tabel")


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Listă Pacienți")

        self.table = QTableWidget()
        self.layoutButtons = QHBoxLayout()
        self.service = TableService()
        self.layout = QVBoxLayout()
        self.buttonGroup = QButtonGroup()

        self.buttons = []
        self.messageBox = None

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
        self.table.setColumnCount(len(coloane))
        self.table.setHorizontalHeaderLabels(coloane)
        self.table.setAlternatingRowColors(True)
        self.table.setUpdatesEnabled(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def fillTable(self):

        date = self.service.initTable()
        self.table.setRowCount(len(date))
        for i in range(0, len(date)):
            k = 1
            for x in date[i].values():
                self.table.setItem(i, k - 1, QTableWidgetItem(str(x)))
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
        self.table.clearSelection()
        deleteWindow = DeletePacientWindow(self.service, coloane)
        if self.service.getLenData() != 0 and deleteWindow.getLinie() is not None:
            self.table.removeRow(deleteWindow.getLinie())
            self.fillTable()

    def pressedAdd(self):
        self.table.clearSelection()
        AddPWindow = AddPacientWindow(self.service, coloane)
        data = AddPWindow.getData()
        if data is not None:
            if int(data['id']) > self.table.rowCount():
                self.table.insertRow(self.table.rowCount())
                self.table.setRowCount(self.table.rowCount())

            k = 1
            for x in coloane:
                self.table.setItem(int(data['id']) - 1, k - 1, QTableWidgetItem(str(data[x])))
                k += 1

    def pressedUpdate(self):
        self.table.clearSelection()
        modifWindow = UpdateWindow(self.service, coloane, self.table.rowCount())
        self.fillTable()

    def pressedSearch(self):
        self.table.clearSelection()
        indexWindow = SearchPacientWindow(self.service, self)
        linie = indexWindow.getLine()
        print(linie)
        if linie is not None:
            self.table.selectRow(linie - 1)
        else:
            self.showMessage()

    def showMessage(self):
        self.messageBox = MessageWindow("Nu exista pacientul")
