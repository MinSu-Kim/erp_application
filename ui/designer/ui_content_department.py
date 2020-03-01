import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

from dto.dto_dept import Department


class DepartmentContent(QWidget):

    def __init__(self, parent=None):
        super(DepartmentContent, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/content_department.ui')
        self.ui = uic.loadUi(ui_path, self)
        self.le_no = self.ui.le_no
        self.le_name = self.ui.le_name
        self.le_floor = self.ui.le_floor

    def get_item(self):
        try:
            dept_no = self.le_no.text()
            dept_name = self.le_name.text()
            floor = self.le_floor.text()
            dept = Department(**{'dept_no': int(dept_no), 'dept_name': dept_name, 'floor': floor})
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


if __name__ == "__main__":
    app = QApplication([])
    w = DepartmentContent()
    w.show()
    sys.exit(app.exec_())