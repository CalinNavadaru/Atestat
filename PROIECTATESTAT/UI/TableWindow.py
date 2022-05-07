from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QWidget, QPushButton, QHBoxLayout, \
    QButtonGroup

from Services.TableService import TableService
from UI.AddPacientWindow import AddPacientWindow
from UI.DeletePacientWindow import DeletePacientWindow
from UI.MessageWindow import MessageWindow
from UI.SearchPacientWindow import SearchPacientWindow
from UI.UpdatePacient import UpdateWindow

coloane = ('Nume', 'Prenume', 'CNP', 'Data nasterii', 'Adresa', 'Cod Asigurat', 'Boli Cronice')
buttonNames = ("Adaugă", "Modificare", "Șterge", "Caută în tabel")


class TableWindow(QWidget):

    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)

        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle("Listă Pacienți")

        self.__table = QTableWidget()
        self.__layoutButtons = QHBoxLayout()
        self.__service = TableService()
        self.__layout = QVBoxLayout()
        self.__buttonGroup = QButtonGroup()

        self.__buttons = []
        self.__messageBox = None

        self.__initButtons()
        self.__createTable()
        self.__fillTable()

        self.__buttonGroup.buttonClicked.connect(self.__handler)

        self.__layoutButtons.setAlignment(QtCore.Qt.AlignLeft)
        self.__layoutButtons.setSpacing(25)

        self.__layout.addLayout(self.__layoutButtons)
        self.__layout.addWidget(self.__table)
        self.setLayout(self.__layout)

        self.show()

    def __initButtons(self):
        k = 1
        for btnName in buttonNames:
            button = QPushButton(btnName, self)
            button.setFont(QFont("Times", 20))
            button.setMaximumSize(250, 100)
            self.__buttonGroup.addButton(button, k)
            self.__layoutButtons.addWidget(button, 1)
            k += 1

    def __createTable(self):
        self.__table.setColumnCount(len(coloane))
        self.__table.setHorizontalHeaderLabels(coloane)
        self.__table.setAlternatingRowColors(True)
        self.__table.setUpdatesEnabled(True)
        self.__table.horizontalHeader().setStretchLastSection(True)
        self.__table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.__table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def __fillTable(self):

        date = self.__service.initTable()
        self.__table.setRowCount(len(date))
        for i in range(0, len(date)):
            k = 1
            for x in date[i].values():
                self.__table.setItem(i, k - 1, QTableWidgetItem(str(x)))
                k += 1

    def __handler(self, button):
        functions = {
            "1": self.__pressedAdd,
            "2": self.__pressedUpdate,
            "3": self.__pressedDelete,
            "4": self.__pressedSearch
        }
        functions[str(self.__buttonGroup.id(button))]()

    def __pressedDelete(self):
        self.__table.clearSelection()
        deleteWindow = DeletePacientWindow(self.__service, coloane)
        if self.__service.getLenData() != 0 and deleteWindow.getLinie() is not None:
            self.__table.removeRow(deleteWindow.getLinie())
            self.__fillTable()

    def __pressedAdd(self):
        self.__table.clearSelection()
        AddPWindow = AddPacientWindow(self.__service, coloane)
        data = AddPWindow.getData()
        if data is not None:
            if int(data['id']) > self.__table.rowCount():
                self.__table.insertRow(self.__table.rowCount())
                self.__table.setRowCount(self.__table.rowCount())

            k = 1
            for x in coloane:
                self.__table.setItem(int(data['id']) - 1, k - 1, QTableWidgetItem(str(data[x])))
                k += 1

    def __pressedUpdate(self):
        self.__table.clearSelection()
        modifWindow = UpdateWindow(self.__service, coloane, self.__table.rowCount())
        self.__fillTable()

    def __pressedSearch(self):
        self.__table.clearSelection()
        indexWindow = SearchPacientWindow(self.__service, self)
        linie = indexWindow.getLine()
        if linie is not None:
            self.__table.selectRow(linie - 1)

    def __showMessage(self):
        self.__messageBox = MessageWindow("Nu exista pacientul")
