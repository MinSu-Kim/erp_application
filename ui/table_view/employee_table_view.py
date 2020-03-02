import inspect

from PyQt5.QtWidgets import QApplication

from dao.employee_dao import EmployeeDao
from dto.dto_emp import Employee
from ui.model.employee_table_model import EmployeeTableModel
from ui.table_view.abstract_table_view import AbstractTableViewWidget


class EmployeeTableViewWidget(AbstractTableViewWidget):
    def __init__(self, parent=None):
        super(EmployeeTableViewWidget, self).__init__(parent)
        self.table_header = self.get_header()
        self.table_data = self.get_data()
        self.model = self.get_model()
        self.tableView.setModel(self.model)

    def get_model(self):
        return EmployeeTableModel(data=self.table_data, header=self.table_header)

    def get_data(self):
        return [tuple(emp)[:-1] for emp in EmployeeDao.instance().select_item()]

    def get_header(self):
        return ['사원번호', '사원명', '성별', '부서', '직속상사', '급여', '직책', '입사일', '증명사진']

    def get_column_size(self):
        return 40, 50, 40, 50, 40, 50, 40, 50, 50

    def get_dto(self, tuple_item):
        print("\n{}({})".format(inspect.stack()[0][3], tuple_item))
        # emp_no, emp_name, title, manager, salary, dept, hire_date, gender, if (pic is not null, 1, 0) as pic
        emp = Employee()
        emp.emp_no = tuple_item[0]
        emp.emp_name = tuple_item[1]
        emp.gender = tuple_item[2]
        emp.dept = tuple_item[3]
        emp.manager = tuple_item[4]
        emp.salary = tuple_item[5]
        emp.title = tuple_item[6]
        emp.hire_date = tuple_item[7]
        emp.pic = tuple_item[8]
        return emp


if __name__ == '__main__':
    app = QApplication([])
    t = EmployeeTableViewWidget()
    t.show()
    app.exec()