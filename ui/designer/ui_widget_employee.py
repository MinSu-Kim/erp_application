import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from dao.employee_dao import EmployeeDao


class EmployeeWidget(QWidget):
    def __init__(self, parent=None):
        super(EmployeeWidget, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/widget_employee.ui')
        self.ui = uic.loadUi(ui_path, self)
        self.employee_item = self.ui.item
        self.employee_table = self.ui.table
        self.set_context_menu(self.employee_table)
        self.setGeometry(100,100, 1200, 600)

    @pyqtSlot()
    def execAddOrUpdate(self):
        employee = self.employee_item.get_item()
        if self.ui.btn_add.text() == '추가':
            try:
                EmployeeDao.instance().insert_item(dto=employee)
                employee.pic = 0 if employee.pic is None else 1
                self.employee_table.add_item(employee)
                self.employee_item.clear_line_edit()
            except Exception as err:
                print(err)
        else:
            try:
                EmployeeDao.instance().update_item(dto=employee)
                employee.pic = 0 if employee.pic is None else 1
                self.employee_table.update_item(self.set_table_idx, employee)
                self.ui.btn_add.setText('추가')
                self.employee_item.clear_line_edit()
            except Exception as err:
                print(err)

    @pyqtSlot()
    def execCancel(self):
        self.employee_item.clear_line_edit()
        self.ui.add_btn.setText('추가')

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
            selcted_item = self.employee_table.get_selected_item()  # {'idx':selected_index.row(), 'item':title}
            EmployeeDao.instance().delete_item(dto=selcted_item['item'])
            self.employee_table.delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def update_item(self):
        dict_employee = self.employee_table.get_selected_item()
        print(dict_employee,'---------------------')
        self.set_table_idx = dict_employee['idx']
        self.employee_item.set_item(dict_employee['item'])
        self.ui.btn_add.setText('수정')


if __name__ == "__main__":
    app = QApplication([])
    w = EmployeeWidget()
    w.show()
    sys.exit(app.exec_())