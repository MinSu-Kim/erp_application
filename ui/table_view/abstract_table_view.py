import inspect
import logging
from abc import abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class AbstractTableViewWidget(QWidget):
    def __init__(self, parent=None):
        super(AbstractTableViewWidget, self).__init__(parent)

        self.logger = logging.getLogger(__name__)
        self.tableView = QTableView()

        # table view 설정
        self.set_table_view_config()
        layout = QGridLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)

    def set_column_size(self):
        column_size = self.get_column_size()
        [self.tableView.horizontalHeader().resizeSection(i, size) for i, size in enumerate(column_size)]

    def set_table_view_config(self):
        # header size
        self.set_column_size()

        self.tableView.horizontalHeader().setStyleSheet('QHeaderView::section{background:#66666666}')  # 배경색을 녹색
        # Set the alignment to the headers
        self.tableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        # 셀 내용 수정불가
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # hide grid
        self.tableView.setShowGrid(True)
        # row단위 선택
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 헤더의 내용을 tableView의 크기에 맞춤
        self.tableView.horizontalHeader().setStretchLastSection(True)

    def delete_item(self, delete_idx):
        self.logger.info("\n{}({})".format(inspect.stack()[0][3], delete_idx))
        try:
            del self.table_data[delete_idx]
            self.model.removeRow(delete_idx)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def add_item(self, title):
        self.logger.info("\n{}({})".format(inspect.stack()[0][3], title))
        try:
            self.table_data.append(tuple(title))
            self.model.insertRow(len(self.table_data) + 1)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    def get_selected_item(self):
        self.logger.info("\n{}() ".format(inspect.stack()[0][3]))
        try:
            selected_row_index = self.tableView.selectedIndexes()[0].row()
            tuple_item = self.table_data[selected_row_index]  # tuple
            item = self.get_dto(tuple_item)
            return {'idx': selected_row_index, 'item': item}
        except Exception as err:
            print(err)

    def update_item(self, idx, title):
        self.logger.info("\n{}({}, {}) ".format(inspect.stack()[0][3], idx, title))
        try:
            self.table_data[idx] = tuple(title)
            self.model.layoutChanged.emit()
        except Exception as err:
            print(err)

    @abstractmethod
    def get_model(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_header(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_column_size(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_dto(self, tuple_item):
        raise NotImplementedError("Subclass must implement abstract method")