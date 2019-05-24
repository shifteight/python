import sys
import argparse
import pandas as pd

from PySide2.QtCore import (QDateTime, QTimeZone, 
	QAbstractTableModel, QModelIndex, QRect, Qt, Slot)
from PySide2.QtGui import QColor, QPainter
from PySide2.QtWidgets import (QAction, QApplication, QHBoxLayout,
	QHeaderView, QMainWindow, QSizePolicy, QTableView, QWidget)
from PySide2.QtCharts import QtCharts


def transform_date(utc, timezone=None):
	utc_fmt = "yyyy-MM-ddTHH:mm:ss.zzzZ"
	new_date = QDateTime().fromString(utc, utc_fmt)
	if timezone:
		new_date.setTimeZone(timezone)
	return new_date

def read_data(fname):
	
	df = pd.read_csv(fname)
	
	df = df.drop(df[df.mag < 0].index)
	magnitudes = df["mag"]

	timezone = QTimeZone(b"Asia/Shanghai")

	times = df["time"].apply(lambda x: transform_date(x, timezone))

	return times, magnitudes


class CustomTableModel(QAbstractTableModel):
	def __init__(self, data=None):
		QAbstractTableModel.__init__(self)
		self.load_data(data)

	def load_data(self, data):
		self.input_dates = data[0].values
		self.input_magnitudes = data[1].values

		self.column_count = 2
		self.row_count = len(self.input_magnitudes)

	def rowCount(self, parent=QModelIndex()):
		return self.row_count

	def columnCount(self, parent=QModelIndex()):
		return slef.column_count

	def headerData(self, section, orientation, role):
		if role != Qt.DisplayRole:
			return None
		if orientation == Qt.Horizontal:
			return ("Date", "Magnitude")[section]
		else:
			return "{}".format(section)

	def data(self, index, role=Qt.DisplayRole):
		column = index.column()
		row = index.row()

		if role == Qt.DisplayRole:
			if column == 0:
				raw_date = self.input_dates[row]
				date = "{}".format(raw_date.toPython())
				return date[:-3]
			elif column == 1:
				return "{:.2f}".format(self.input_magnitudes[row])
		elif role == Qt.BackgroundRole:
			return QColor(Qt.white)
		elif role == Qt.TextAlignmentRole:
			return Qt.AlignRight

		return None

class Widget(QWidget):
	def __init__(self, data):
		QWidget.__init__(self)

		self.model = CustomTableModel(data)

		self.table_view = QTableView()
		self.tablle_view

class MainWindow(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		self.setWindowTitle("Earthquake information")

		self.menu = self.menuBar()
		self.file_menu = self.menu.addMenu("File")

		exit_action = QAction("Exit", self)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.triggered.connect(self.exit_app)

		self.file_menu.addAction(exit_action)

		self.status = self.statusBar()
		self.status.showMessage("Data loaded and plotted")

		geometry = app.desktop().availableGeometry(self)
		self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

	@Slot()
	def exit_app(self, checked):
		sys.exit()


if __name__ == '__main__':
    options = argparse.ArgumentParser()
    options.add_argument("-f", "--file", type=str, required=True)
    args = options.parse_args()
    data = read_data(args.file)
    
    app =QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
