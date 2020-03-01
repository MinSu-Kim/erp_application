from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

from dto.dto_dept import Department


class DepartmentContentWidget(QWidget):
    def __init__(self, parent=None):
        super(DepartmentContentWidget, self).__init__(parent)
        root_layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(root_layout)
        self.init_component(root_layout)

    def init_component(self, root_layout):
        item_size = QSize(0, 40)

        self.lbl_no = QLabel('부서 번호', self)
        self.lbl_no.setAlignment(Qt.AlignCenter)
        self.lbl_no.setMinimumSize(item_size)
        self.lbl_name = QLabel('부서명', self)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setMinimumSize(item_size)
        self.lbl_floor = QLabel('위치', self)
        self.lbl_floor.setAlignment(Qt.AlignCenter)
        self.lbl_floor.setMinimumSize(item_size)

        self.le_no = QLineEdit()
        self.le_no.setMinimumSize(item_size)
        self.le_name = QLineEdit()
        self.le_name.setMinimumSize(item_size)
        self.le_floor = QLineEdit()
        self.le_floor.setMinimumSize(item_size)

        echo_group = QGroupBox('부서', self)
        group_layout = QGridLayout()
        echo_group.setLayout(group_layout)
        group_layout.addWidget(self.lbl_no,    0, 0, 1, 1)
        group_layout.addWidget(self.le_no,     0, 1, 1, 1)
        group_layout.addWidget(self.lbl_name,  1, 0, 1, 1)
        group_layout.addWidget(self.le_name,   1, 1, 1, 1)
        group_layout.addWidget(self.lbl_floor, 2, 0, 1, 1)
        group_layout.addWidget(self.le_floor,  2, 1, 1, 1)

        root_layout.addWidget(echo_group)

    def get_item(self):
        try:
            dept_no = self.le_no.text()
            dept_name = self.le_name.text()
            floor = self.le_floor.text()
            dept = Department(**{'dept_no': int(dept_no), 'dept_name': dept_name, 'floor':floor})
            print(dept)
            return dept;
        except Exception as err:
            print(err)

    def set_item(self, dept):
        self.le_no.setText(str(dept.dept_no))
        self.le_name.setText(dept.dept_name)
        self.le_floor.setText(str(dept.floor))

    def clear_line_edit(self):
        self.le_no.setText('')
        self.le_name.setText('')
        self.le_floor.setText('')


if __name__ == '__main__':
    app = QApplication([])
    t = DepartmentContentWidget()
    t.show()
    app.exec()
