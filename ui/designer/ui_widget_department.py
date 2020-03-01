import inspect
import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from dao.department_dao import DepartmentDao
from dao.title_dao import TitleDao


class DepartmentWidget(QWidget):
    def __init__(self, parent=None):
        super(DepartmentWidget, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/department_widget.ui')
        self.ui = uic.loadUi(ui_path, self)
        self.dept_item = self.ui.item
        self.dept_table = self.ui.table
        self.set_context_menu(self.dept_table)

    @pyqtSlot()
    def execAddOrUpdate(self):
        print('execAddOrUpdate')
        department = self.dept_item.get_item()
        if self.ui.btn_add.text() == '추가':
            try:
                DepartmentDao.instance().insert_item(dto=department)
                self.dept_table.add_item(department)
                self.dept_item.clear_line_edit()
            except Exception as err:
                raise err
        else:
            try:
                DepartmentDao.instance().update_item(dto=department)
                self.dept_table.update_item(self.set_table_idx, department)
                self.ui.btn_add.setText('추가')
                self.dept_item.clear_line_edit()
            except Exception as err:
                raise err

    @pyqtSlot()
    def execCancel(self):
        self.dept_item.clear_line_edit()

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
            selcted_item = self.dept_table.get_selected_item()  # {'idx':selected_index.row(), 'item':title}
            DepartmentDao.instance().delete_item(dto=selcted_item['item'])
            self.dept_table.delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def update_item(self):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        dict_department = self.dept_table.get_selected_item()
        print(dict_department,'---------------------')
        self.set_table_idx = dict_department['idx']

        self.dept_item.set_item(dict_department['item'])
        self.ui.btn_add.setText('수정')


if __name__ == "__main__":
    app = QApplication([])
    w = DepartmentWidget()
    w.show()
    sys.exit(app.exec_())