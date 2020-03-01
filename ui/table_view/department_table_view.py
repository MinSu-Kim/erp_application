import inspect

from PyQt5.QtWidgets import QApplication

from dao.department_dao import DepartmentDao
from dto.dto_dept import Department
from ui.model.department_table_model import DepartmentTableModel
from ui.table_view.abstract_table_view import AbstractTableViewWidget


class DepartmentTableViewWidget(AbstractTableViewWidget):
    def __init__(self, parent=None):
        super(DepartmentTableViewWidget, self).__init__(parent)
        self.table_header = self.get_header()
        self.table_data = self.get_data()
        self.model = self.get_model()
        self.tableView.setModel(self.model)

    def get_model(self):
        return DepartmentTableModel(data=self.table_data, header=self.table_header)

    def get_data(self):
        return [tuple(dept) for dept in DepartmentDao.instance().select_item()]

    def get_header(self):
        return ['부서 코드', '부서명', '위치']

    def get_column_size(self):
        return 100, 100, 50

    def get_dto(self, tuple_item):
        self.logger.info("\n{}({})".format(inspect.stack()[0][3], tuple_item))
        dept = Department()
        dept.dept_no = tuple_item[0]
        dept.dept_name = tuple_item[1]
        dept.floor = tuple_item[2]
        return dept


if __name__ == '__main__':
    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = DepartmentTableViewWidget()
    t.show()
    app.exec()