from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
from PyQt5.uic import loadUi
import sys
import sqlite3
import os


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Vechicle")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Insert Vehicle Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.QBtn.clicked.connect(self.addvehicle)

        layout = QVBoxLayout()

        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("vehicle Name")
        layout.addWidget(self.nameinput)

        self.branchinput = QComboBox()
        self.branchinput.addItem("Car A/C -  number of passengers - 3 and 4 ")
        self.branchinput.addItem("Car non A/C -  number of passengers - 3 and 4 ")
        self.branchinput.addItem("Van A/C - number of passengers - 6 and 8 ")
        self.branchinput.addItem("Van non A/C - number of passengers - 6 and 8 ")
        self.branchinput.addItem("3 Wheelers - Maximum number of passengers - 3")
        self.branchinput.addItem("Trucks - Size – 7 ft and 12 ft ")
        self.branchinput.addItem("Lorry - Max load and size -  2500kg  and 3500kg ")
        layout.addWidget(self.branchinput)

        self.seminput = QComboBox()
        self.seminput.addItem("1")
        self.seminput.addItem("2")
        self.seminput.addItem("3")
        self.seminput.addItem("4")
        self.seminput.addItem("5")
        self.seminput.addItem("6")
        self.seminput.addItem("7")
        self.seminput.addItem("8")
        self.seminput.addItem("9")
        self.seminput.addItem("10")
        self.seminput.addItem("11")
        self.seminput.addItem("12")
        self.seminput.addItem("13")
        self.seminput.addItem("14")
        self.seminput.addItem("15")
        self.seminput.addItem("16")
        self.seminput.addItem("17")
        self.seminput.addItem("18")
        self.seminput.addItem("19")
        self.seminput.addItem("20")
        self.seminput.addItem("21")
        self.seminput.addItem("22")
        self.seminput.addItem("23")
        self.seminput.addItem("24")
        self.seminput.addItem("25")
        self.seminput.addItem("26")
        self.seminput.addItem("27")
        self.seminput.addItem("28")
        self.seminput.addItem("29")
        self.seminput.addItem("30")
        self.seminput.addItem("31")
        self.seminput.addItem("32")
        self.seminput.addItem("33")
        self.seminput.addItem("34")
        self.seminput.addItem("35")
        self.seminput.addItem("36")

        layout.addWidget(self.seminput)

        self.Vehiclenoinput = QLineEdit()
        self.Vehiclenoinput.setPlaceholderText("Vehicle Number")
        layout.addWidget(self.Vehiclenoinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addvehicle(self):

        vehicle_name = ""
        branch = ""
        sem = -1
        Vehicleno = ""
        address = ""

        vehicle_name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        Vehicleno = self.Vehiclenoinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database1.db")
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO booking(Reg_id,name,branch,sem,address) VALUES (?,?,?,?,?)",
                           (sem, vehicle_name, branch, Vehicleno, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Vehicle is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add vehicle to the database.')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search Vehicle")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchvehicle)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Reg_id")  # search place holder
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchvehicle(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database1.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from booking WHERE Reg_id=" + str(searchrol))  # db search connection
            row = result.fetchone()
            serachresult = "Reg id : " + str(row[0]) + '\n' + "Vehicle Name : " + str(row[1]) + '\n' + "Type : " + str(
                row[2]) + '\n' + "Vehicle Number : " + str(row[3]) + \
                           '\n' + "Address : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find vehicle from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Vehicle")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletevehicle)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Reg id.")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletevehicle(self):

        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database1.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from booking WHERE Reg_id=" + str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(), 'Successful', 'Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete vehicle from the database.')


class BookDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(BookDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Booking")

        self.setWindowTitle("Search Vehicle")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.bookvehicle)  #
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Reg_id")  # search place holder
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def bookvehicle(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database1.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from booking WHERE Reg_id=" + str(searchrol))  # db search connection
            row = result.fetchone()
            serachresult = "Reg id : " + str(row[0]) + '\n' + "Vehicle Name : " + str(row[1]) + '\n' + "Type : " + str(
                row[2]) + '\n' + "Vehicle number : " + str(row[3]) + \
                           '\n' + "Address : " + str(row[4])
            QMessageBox.information(QMessageBox(), 'Book Successful', serachresult)
            # self.c.execute("DELETE from booking WHERE Reg_id=" + str(delrol))  #remove data
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find vehicle from the database.')


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        self.setFixedWidth(500)
        self.setFixedHeight(250)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        self.setWindowTitle("About")
        title = QLabel("Car boooking system")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/dexter.jpg')
        pixmap = pixmap.scaledToWidth(275)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(150)

        layout.addWidget(title)

        layout.addWidget(QLabel("v2.0"))
        layout.addWidget(QLabel("Copyrights belongs to Steffan "))
        layout.addWidget(labelpic)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setWindowIcon(QIcon('icon/g2.png'))  #window icon

        self.conn = sqlite3.connect("database1.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS booking(Reg_id INTEGER PRIMARY KEY AUTOINCREMENT ,"
                       "name TEXT,branch TEXT,sem INTEGER,address TEXT)")
        self.c.close()

        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("Cab Booking")
        self.setMinimumSize(800, 600)

        book_menu = self.menuBar().addMenu("&booking")
        self.setWindowTitle("Booking")
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.setHorizontalHeaderLabels(("Reg id", "vehicle Name", "Type", "vehicle number", "Address"))

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_addvehicle = QAction(QIcon("icon/cr.png"), "Add Vehicle", self)  # add vehicle icon
        btn_ac_addvehicle.triggered.connect(self.insert)
        btn_ac_addvehicle.setStatusTip("Add Vehicle")
        toolbar.addAction(btn_ac_addvehicle)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"), "Refresh", self)  # refresh icon
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  # search icon
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search Vehicle")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete Vehicle")
        toolbar.addAction(btn_ac_delete)

        # booking

        btn_ac_booking = QAction(QIcon("icon/download.png"), "Booking", self)
        btn_ac_booking.triggered.connect(self.booking)
        btn_ac_booking.setStatusTip("Book Vehicle")
        toolbar.addAction(btn_ac_booking)

        addvehicle_action = QAction(QIcon("icon/cr.png"), "Insert Vehicle", self)
        addvehicle_action.triggered.connect(self.insert)
        file_menu.addAction(addvehicle_action)

        searchvehicle_action = QAction(QIcon("icon/s1.png"), "Search Vehicle ", self)
        searchvehicle_action.triggered.connect(self.search)
        file_menu.addAction(searchvehicle_action)

        delvehicle_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        delvehicle_action.triggered.connect(self.delete)
        file_menu.addAction(delvehicle_action)

        about_action = QAction(QIcon("icon/i1.png"), "Developer", self)  # info icon
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect("database1.db")
        query = "SELECT * FROM booking"
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def WelcomeScreen(self):
        dlg = WelcomeDialog()
        dlg.exec_()

    def CreateDialog(self):
        dlg = CreateDialog()
        dlg.exec_()

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def booking(self):
        dlg = BookDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

app = QApplication(sys.argv)
if(QDialog.Accepted == True):

    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
