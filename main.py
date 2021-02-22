import sys
import sqlite3

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QMainWindow, QTableWidgetItem, \
    QAbstractScrollArea
from PyQt5 import uic


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.select_data()

    def select_data(self):
        query = "SELECT ID, sort, roast_level.name_roast, type.name, description, cost, volume " \
                "FROM coffee INNER JOIN roast_level ON roast_level.id_roast = coffee.roast INNER " \
                "JOIN type ON type.id_type = type"
        res = self.connection.cursor().execute(query).fetchall()
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setColumnCount(len(res[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'Сорт', 'Степень обжарки', 'Молотый/В зернах', 'Описание вкуса', 'Цена',
             'Объем упаковки'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
