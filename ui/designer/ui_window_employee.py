import inspect
import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import *

from dao.title_dao import TitleDao


class TitleWindow(QMainWindow):

    def __init__(self, parent=None):
        super(TitleWindow, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/employee_window.ui')
        self.ui = uic.loadUi(ui_path, self)

        self.title_item = self.ui.content
        self.table_view = self.ui.table
        self.set_context_menu(self.table_view)

    @pyqtSlot()
    def execCancel(self):
        self.title_item.clear_line_edit()

    @pyqtSlot()
    def execAddOrUpdate(self):
        print('execAddOrUpdate')
        title = self.title_item.get_item()
        if self.ui.btn_add.text() == '추가':
            try:
                TitleDao.instance().insert_item(dto=title)
                self.table_view.add_item(title)
                self.title_item.clear_line_edit()
            except Exception as err:
                raise err
        else:
            try:
                TitleDao.instance().update_item(dto=title)
                self.table_view.update_item(self.set_table_idx, title)
                self.ui.btn_add.setText('추가')
                self.title_item.clear_line_edit()
            except Exception as err:
                raise err

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)

        update_action.triggered.connect(self.update_item)
        delete_action.triggered.connect(self.delete_item)

    def delete_item(self):
        try:
            selcted_item = self.table_view.get_selected_item()  # {'idx':selected_index.row(), 'item':title}
            TitleDao.instance().delete_item(dto=selcted_item['item'])
            self.table_view.delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def update_item(self):
        dict_title = self.table_view.get_selected_item()
        print(dict_title, '---------------------')
        self.set_table_idx = dict_title['idx']
        self.title_item.set_item(dict_title['item'])
        self.ui.btn_add.setText('수정')


if __name__ == "__main__":
    app = QApplication([])
    w = TitleWindow()
    w.show()
    sys.exit(app.exec_())