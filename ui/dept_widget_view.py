import inspect

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


from dao.department_dao import DepartmentDao
from ui.content.dept_content_view import DepartmentContentWidget
from ui.table_view.department_table_view import DepartmentTableViewWidget


class DepartmentWidgetView(QWidget):
    def __init__(self):
        super().__init__()
        self.dept_item = DepartmentContentWidget()
        self.table_view = DepartmentTableViewWidget()
        self.set_table_idx = None

        self.add_btn = QPushButton('추가')
        self.cancel_btn = QPushButton('취소')

        layout_insert = QHBoxLayout()
        layout_insert.addSpacerItem(QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout_insert.addWidget(self.add_btn)
        layout_insert.addWidget(self.cancel_btn)
        layout_insert.setContentsMargins(10, 0, 10, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.dept_item)
        layout.addLayout(layout_insert)
        layout.addWidget(self.table_view)

        self.setLayout(layout)
        self.set_context_menu(self.table_view)
        self.add_btn.clicked.connect(self.add_item)
        self.cancel_btn.clicked.connect(self.clear_item)

        self.setGeometry(300, 300, 500, 400) # 창의 좌표(x, y) 크기(width, height)

        # self.show()

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
            selcted_item = self.table_view.get_selected_item() # {'idx':selected_index.row(), 'item':title}
            DepartmentDao.instance().delete_item(dto=selcted_item['item'])
            self.table_view.delete_item(selcted_item['idx'])
        except Exception as err:
            raise err

    def add_item(self):
        dept = self.dept_item.get_item()
        if self.add_btn.text() == '추가':
            try:
                DepartmentDao.instance().insert_item(dto=dept)
                self.table_view.add_item(dept)
                self.dept_item.clear_line_edit()
            except Exception as err:
                raise err
        else:
            try:
                DepartmentDao.instance().update_item(dto=dept)
                self.table_view.update_item(self.set_table_idx, dept)
                self.add_btn.setText('추가')
                self.dept_item.clear_line_edit()
            except Exception as err:
                raise err

    def update_item(self):
        print("\n______ {}() ______".format(inspect.stack()[0][3]))
        dict_dept = self.table_view.get_selected_item()
        self.set_table_idx = dict_dept['idx']
        self.dept_item.set_item(dict_dept['item'])
        self.add_btn.setText('수정')

    def clear_item(self):
        self.title_item.clear_line_edit()


if __name__ == '__main__':
    app = QApplication([])
    window = DepartmentWidgetView()
    window.show()
    app.exec()