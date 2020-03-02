from PyQt5.QtWidgets import *

from ui.dept_widget_view import DepartmentWidgetView
from ui.employee_widget_view import EmployeeWidgetView
from ui.title_widget_view import TitleWidgetView


class ErpMain(QMainWindow):
    def __init__(self):
        super().__init__()
        tabWidget = QTabWidget()
        title = TitleWidgetView()
        tabWidget.addTab(title, '직책')
        dept = DepartmentWidgetView()
        tabWidget.addTab(dept, '부서')
        emp = EmployeeWidgetView()
        tabWidget.addTab(emp, '사원')
        tabWidget.setCurrentIndex(0)
        self.setCentralWidget(tabWidget)


if __name__ == "__main__":
    app = QApplication([])
    w = ErpMain()
    w.show()
    app.exec_()