import inspect
from builtins import print

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from dao.employee_dao import EmployeeDao
from ui.content.emp_content_view import EmployeeContentWidget
from ui.table_view.employee_table_view import EmployeeTableViewWidget


class EmployeeWidgetView(QWidget):
    def __init__(self):
        super().__init__()
        self.employee_item = EmployeeContentWidget()
        self.employee_table = EmployeeTableViewWidget()
        self.set_table_idx = None

        self.add_btn = QPushButton('추가')
        self.cancel_btn = QPushButton('취소')

        layout_insert = QHBoxLayout()
        layout_insert.addSpacerItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout_insert.addWidget(self.add_btn)
        layout_insert.addWidget(self.cancel_btn)
        layout_insert.setContentsMargins(10, 0, 10, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.employee_item)
        layout.addLayout(layout_insert)
        layout.addWidget(self.employee_table)

        self.setLayout(layout)
        self.set_context_menu(self.employee_table)
        self.add_btn.clicked.connect(self.add_item)
        self.cancel_btn.clicked.connect(self.clear_item)

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
        self.add_btn.setText('수정')

    def add_item(self):
        employee = self.employee_item.get_item()
        if self.add_btn.text() == '추가':
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
                self.add_btn.setText('추가')
                self.employee_item.clear_line_edit()
            except Exception as err:
                print(err)

    def clear_item(self):
        self.emp_item.clear_line_edit()
        self.add_btn.setText('추가')


if __name__ == '__main__':
    app = QApplication([])
    window = EmployeeWidgetView()
    window.show()
    app.exec()