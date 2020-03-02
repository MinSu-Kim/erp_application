import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtCore import Qt, QDate, QBuffer, QByteArray, QIODevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from dao.department_dao import DepartmentDao
from dao.employee_dao import EmployeeDao
from dao.title_dao import TitleDao
from dto.dto_emp import Employee


class EmployeeContent(QWidget):

    def __init__(self, parent=None):
        super(EmployeeContent, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/content_employee.ui')
        self.ui = uic.loadUi(ui_path, self)

        self.ui.de_hire_date.setDate(QDate.currentDate())

        self.title_list = TitleDao.instance().select_item()
        title_name_list = [title.title_name for title in self.title_list]
        self.ui.cb_title.addItems(title_name_list)
        self.ui.cb_title.setCurrentIndex(-1)

        self.dept_list = DepartmentDao.instance().select_item()
        dept_name_list = [dept.dept_name for dept in self.dept_list]
        self.ui.cb_dept.addItems(dept_name_list)
        self.ui.cb_dept.setCurrentIndex(-1)

        self.ui.cb_dept.currentTextChanged.connect(self.on_cmb_dept_changed)
        self.ui.le_pass1.textChanged.connect(self.passwd_valid_check)
        self.ui.le_pass2.textChanged.connect(self.passwd_valid_check)
        self.ui.lbl_img.mousePressEvent = self.file_open

    def file_open(self, event):
        self.file_name = QFileDialog.getOpenFileName(self)[0]
        pixmap = QPixmap()
        pixmap.load(self.file_name)
        self.ui.lbl_img.setPixmap(pixmap.scaled(100, 150, Qt.KeepAspectRatio))

    def passwd_valid_check(self):
        if self.ui.le_pass1.text() == self.le_pass2.text():
            self.ui.lbl_pass_confirm.setText("일치")
        else:
            self.ui.lbl_pass_confirm.setText("불일치")

    def on_cmb_dept_changed(self, value):
        for dept in self.dept_list:
            if value == dept.dept_name:
                self.mgn_list_by_dept = EmployeeDao.instance().select_item(
                    sql='select emp_no, emp_name, dept from employee where dept = %s or title = 1', dto=dept)
                mgn_list = ['{}({})'.format(mgr.emp_name, mgr.emp_no) for mgr in self.mgn_list_by_dept]
                self.ui.cb_manager.clear()
                self.ui.cb_manager.addItems(mgn_list)
                self.ui.cb_manager.setCurrentIndex(-1)

    def get_item(self):
        try:
            emp = Employee()
            emp.emp_no = int(self.ui.le_no.text())
            emp.emp_name = self.ui.le_name.text()
            emp.salary = self.ui.sp_salary.value()
            emp.passwd = self.ui.le_pass1.text()
            # emp.hire_date = self.de_hire_date.date().toString("yyyy-MM-dd")
            emp.hire_date = self.ui.de_hire_date.dateTime().toPyDateTime()
            emp.gender = 1 if self.ui.rb_male.isChecked() else 0
            emp.dept = [dept.dept_no for dept in self.dept_list if self.ui.cb_dept.currentText() == dept.dept_name][0]
            emp.manager = int(self.ui.cb_manager.currentText()[4:-1])  # '조민희(1003)'-> 1003
            emp.title = [title.title_no for title in self.title_list if self.ui.cb_title.currentText() == title.title_name][0]

            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            pixmap = self.ui.lbl_img.pixmap()
            pixmap.save(buff, 'PNG')
            pixmap_bytes = ba.data()

            emp.pic = pixmap_bytes

            return emp
        except Exception as err:
            print(err)

    def set_item(self, emp):
        try:
            self.ui.le_no.setText(str(emp.emp_no))
            self.ui.le_name.setText(emp.emp_name)
            self.ui.sp_salary.setValue(emp.salary)
            self.ui.le_pass1.setText('')
            self.ui.le_pass2.setText('')
            self.ui.lbl_pass_confirm.setText('')

            print(emp.get_to_dict())
            print('emp.hire_date', type(emp.hire_date), emp.hire_date)

            self.ui.de_hire_date.setDate(emp.hire_date)
            if emp.gender == 1:
                self.ui.rb_male.setChecked(True)
            else:
                self.ui.rb_female.setChecked(True)
            self.ui.cb_dept.clear()
            self.ui.cb_dept.addItems([dept.dept_name for dept in self.dept_list])
            [self.ui.cb_dept.setCurrentText(dept.dept_name) for dept in self.dept_list if emp.dept == dept.dept_no]
            [self.ui.cb_manager.setCurrentText('{}({})'.format(manager.emp_name, manager.emp_no)) for manager in
             self.mgn_list_by_dept if emp.manager == manager.emp_no]
            [self.ui.cb_title.setCurrentText(title.title_name) for title in self.title_list if emp.title == title.title_no]

            emp_pic = QPixmap()
            if emp.pic == 1:
                emp = EmployeeDao.instance().select_pic_by_empno(dto=emp)[0]
                emp_pic.loadFromData(emp.pic)
            else:
                emp_pic = QPixmap(pkg_resources.resource_filename('resources', 'no_img.png'))
            self.ui.lbl_img.setPixmap(emp_pic.scaled(100, 150, Qt.KeepAspectRatio))
        except Exception as err:
            print(err)

    def clear_line_edit(self):
        self.ui.le_no.setText('')
        self.ui.le_name.setText('')
        self.ui.sp_salary.setValue(1500000)
        self.ui.le_pass1.setText('')
        self.ui.le_pass2.setText('')
        self.ui.lbl_pass_confirm.setText('')
        self.ui.de_hire_date.setDate(QDate.currentDate())
        self.ui.rb_male.setChecked(True)
        self.ui.cb_dept.clear()
        self.ui.cb_dept.addItems([dept.dept_name for dept in self.dept_list])
        self.ui.cb_dept.setCurrentIndex(-1)
        self.ui.cb_manager.clear()
        self.ui.cb_manager.setCurrentIndex(-1)
        self.ui.cb_title.setCurrentIndex(-1)
        pixmap = QPixmap(pkg_resources.resource_filename('resources', 'no_img.png'))
        self.ui.lbl_img.setPixmap(pixmap.scaled(100, 150, Qt.KeepAspectRatio))


if __name__ == "__main__":
    app = QApplication([])
    w = EmployeeContent()
    w.show()
    sys.exit(app.exec_())