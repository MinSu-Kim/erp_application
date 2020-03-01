from PyQt5.QtCore import Qt, QSize, QDate, QBuffer, QByteArray, QIODevice
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from dao.department_dao import DepartmentDao
from dao.employee_dao import EmployeeDao
from dao.title_dao import TitleDao
from dto.dto_emp import Employee


class EmployeeContentWidget(QWidget):
    def __init__(self):
        super().__init__()
        root_layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(root_layout)
        self.init_component(root_layout)

    def init_component(self, root_layout):
        item_size = QSize(150, 40)
        self.file_name = 'no_img.png'

        self.lbl_no = QLabel('사원 번호', self)
        self.lbl_no.setAlignment(Qt.AlignCenter)
        self.lbl_no.setMinimumSize(item_size)
        self.le_no = QLineEdit()
        self.le_no.setMinimumSize(item_size)

        self.lbl_name = QLabel('사원명', self)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setMinimumSize(item_size)
        self.le_name = QLineEdit()
        self.le_name.setMinimumSize(item_size)

        self.lbl_gender = QLabel('성별', self)
        self.lbl_gender.setAlignment(Qt.AlignCenter)
        self.lbl_gender.setMinimumSize(item_size)

        layout_gender = QHBoxLayout()
        self.rb_male = QRadioButton('남', self)
        self.rb_male.setChecked(True)
        # self.rb_male.setMinimumSize(item_size)
        layout_gender.addWidget(self.rb_male)

        self.rb_female = QRadioButton('여', self)
        # self.rb_female.setMinimumSize(item_size)
        layout_gender.addWidget(self.rb_female)

        btn_group = QButtonGroup()
        btn_group.addButton(self.rb_male)
        btn_group.addButton(self.rb_female)
        # layout_gender.setContentsMargins(10, 0, 10, 0)

        #직속상사
        self.lbl_manager = QLabel('직속 상사', self)
        self.lbl_manager.setAlignment(Qt.AlignCenter)
        self.lbl_manager.setMinimumSize(item_size)

        self.cb_manager = QComboBox(self)
        self.cb_manager.setMinimumSize(item_size)
        self.cb_manager.setCurrentIndex(-1)

        # 급여
        self.lbl_salary = QLabel('급여', self)
        self.lbl_salary.setAlignment(Qt.AlignCenter)
        self.lbl_salary.setMinimumSize(item_size)

        self.sp_salary = QSpinBox()
        self.sp_salary.setMinimumSize(item_size)
        self.sp_salary.setRange(1500000, 5000000)
        self.sp_salary.setSingleStep(100000)
        self.sp_salary.setGroupSeparatorShown(True);
        self.sp_salary.setAlignment(Qt.AlignRight)
        echo_group = QGroupBox('사원', self)

        #부서
        self.lbl_dept = QLabel('부서', self)
        self.lbl_dept.setAlignment(Qt.AlignCenter)
        self.lbl_dept.setMinimumSize(item_size)

        self.cb_dept = QComboBox(self)
        self.cb_dept.setMinimumSize(item_size)

        self.dept_list = DepartmentDao.instance().select_item()
        dept_name_list = [dept.dept_name for dept in self.dept_list]
        self.cb_dept.addItems(dept_name_list)
        self.cb_dept.setCurrentIndex(-1)

        # 입사일
        self.lbl_hire_date = QLabel('입사일', self)
        self.lbl_hire_date.setAlignment(Qt.AlignCenter)
        self.lbl_hire_date.setMinimumSize(item_size)

        self.de_hire_date = QDateEdit(self)
        self.de_hire_date.setMinimumSize(item_size)
        self.de_hire_date.setDate(QDate.currentDate())
        self.de_hire_date.setMinimumDate(QDate(1900, 1, 1))
        self.de_hire_date.setMaximumDate(QDate(2100, 12, 31))
        self.de_hire_date.setDisplayFormat('yyyy-MM-dd')
        self.de_hire_date.setAlignment(Qt.AlignCenter)

        # 직책
        self.lbl_title = QLabel('직책', self)
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setMinimumSize(item_size)

        self.cb_title = QComboBox(self)
        self.cb_title.setMinimumSize(item_size)
        self.title_list = TitleDao.instance().select_item()
        title_name_list = [title.title_name for title in self.title_list]
        self.cb_title.addItems(title_name_list)
        self.cb_title.setCurrentIndex(-1)

        #비밀번호
        self.lbl_pass1 = QLabel('비밀 번호', self)
        self.lbl_pass1.setAlignment(Qt.AlignCenter)
        self.lbl_pass1.setMinimumSize(item_size)

        self.le_pass1 = QLineEdit()
        self.le_pass1.setEchoMode(QLineEdit.Password)
        self.le_pass1.setMinimumSize(item_size)

        self.lbl_pass2 = QLabel('비밀 번호 확인', self)
        self.lbl_pass2.setAlignment(Qt.AlignCenter)
        self.lbl_pass2.setMinimumSize(item_size)
        self.le_pass2 = QLineEdit()
        self.le_pass2.setEchoMode(QLineEdit.Password)
        self.le_pass2.setMinimumSize(item_size)

        self.lbl_pass_confirm = QLabel('', self)
        self.lbl_pass_confirm.setStyleSheet('color: red')
        self.lbl_pass_confirm.setAlignment(Qt.AlignCenter)
        self.lbl_pass_confirm.setMinimumSize(item_size)

        #사진
        self.lbl_img = QLabel()
        self.lbl_img.setMinimumSize(QSize(200, 275))
        self.lbl_img.setAlignment(Qt.AlignCenter)
        self.lbl_img.setFrameShape(QFrame.Box)
        self.lbl_img.setFrameShadow(QFrame.Sunken)

        pixmap = QPixmap(self.file_name)
        self.lbl_img.setPixmap(pixmap.scaled(150, 275, Qt.KeepAspectRatio))

        self.btn_pic = QPushButton('사진 추가')
        self.btn_pic.setMinimumSize(item_size)

        group_layout = QGridLayout()
        echo_group.setLayout(group_layout)
        group_layout.addWidget(self.lbl_no,           0, 0, 1, 1)
        group_layout.addWidget(self.le_no,            0, 1, 1, 1)
        group_layout.addWidget(self.lbl_name,         1, 0, 1, 1)
        group_layout.addWidget(self.le_name,          1, 1, 1, 1)
        group_layout.addWidget(self.lbl_salary,       2, 0, 1, 1)
        group_layout.addWidget(self.sp_salary,        2, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass1,        3, 0, 1, 1)
        group_layout.addWidget(self.le_pass1,         3, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass2,        4, 0, 1, 1)
        group_layout.addWidget(self.le_pass2,         4, 1, 1, 1)
        group_layout.addWidget(self.lbl_pass_confirm, 5, 1, 1, 1)

        group_layout.addWidget(self.lbl_hire_date,    0, 2, 1, 1)
        group_layout.addWidget(self.de_hire_date,     0, 3, 1, 1)
        group_layout.addWidget(self.lbl_gender,       1, 2, 1, 1)
        group_layout.addLayout(layout_gender,         1, 3, 1, 1)
        group_layout.addWidget(self.lbl_dept,         2, 2, 1, 1)
        group_layout.addWidget(self.cb_dept,          2, 3, 1, 1)
        group_layout.addWidget(self.lbl_manager,      3, 2, 1, 1)
        group_layout.addWidget(self.cb_manager,       3, 3, 1, 1)
        group_layout.addWidget(self.lbl_title,        4, 2, 1, 1)
        group_layout.addWidget(self.cb_title,         4, 3, 1, 1)

        group_layout.addWidget(self.lbl_img,               0, 5, 4, 1)
        group_layout.addWidget(self.btn_pic,          4, 5, 1, 1)

        horizontalSpacer = QSpacerItem(150, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        group_layout.addItem(horizontalSpacer,          0, 4, 1, 1)

        self.cb_dept.currentTextChanged.connect(self.on_cmb_dept_changed)
        self.le_pass1.textChanged.connect(self.passwd_valid_check)
        self.le_pass2.textChanged.connect(self.passwd_valid_check)
        self.btn_pic.clicked.connect(self.file_open)
        root_layout.addWidget(echo_group)

    def file_open(self):
        self.file_name = QFileDialog.getOpenFileName(self)[0]
        pixmap = QPixmap()
        pixmap.load(self.file_name)
        self.lbl_img.setPixmap(pixmap.scaled(150, 275, Qt.KeepAspectRatio))

    def passwd_valid_check(self):
        if self.le_pass1.text() == self.le_pass2.text():
            self.lbl_pass_confirm.setText("일치")
        else:
            self.lbl_pass_confirm.setText("불일치")

    def on_cmb_dept_changed(self, value):
        for dept in self.dept_list:
            if value == dept.dept_name:
                self.mgn_list_by_dept = EmployeeDao.instance().select_item(sql='select emp_no, emp_name, dept from employee where dept = %s or manager is null', dto=dept)
                mgn_list = ['{}({})'.format(mgr.emp_name, mgr.emp_no) for mgr in self.mgn_list_by_dept]
                self.cb_manager.clear()
                self.cb_manager.addItems(mgn_list)
                self.cb_manager.setCurrentIndex(-1)

    def get_item(self):
        try:
            emp = Employee()
            emp.emp_no = int(self.le_no.text())
            emp.emp_name = self.le_name.text()
            emp.salary = self.sp_salary.value()
            emp.passwd = self.le_pass1.text()
            # emp.hire_date = self.de_hire_date.date().toString("yyyy-MM-dd")
            emp.hire_date = self.de_hire_date.dateTime().toPyDateTime()
            emp.gender = 1 if self.rb_male.isChecked() else 0
            emp.dept = [dept.dept_no for dept in self.dept_list if self.cb_dept.currentText() == dept.dept_name][0]
            emp.manager = int(self.cb_manager.currentText()[4:-1]) #'조민희(1003)'-> 1003
            emp.title = [title.title_no for title in self.title_list if self.cb_title.currentText() == title.title_name][0]

            ba = QByteArray()
            buff = QBuffer(ba)
            buff.open(QIODevice.WriteOnly)
            pixmap = self.lbl_img.pixmap()
            pixmap.save(buff, 'PNG')
            pixmap_bytes = ba.data()

            emp.pic = pixmap_bytes

            return emp
        except Exception as err:
            print(err)

    def set_item(self, emp):
        self.le_no.setText(str(emp.emp_no))
        self.le_name.setText(emp.emp_name)
        self.sp_salary.setValue(emp.salary)
        self.le_pass1.setText('')
        self.le_pass2.setText('')
        self.lbl_pass_confirm.setText('')
        self.de_hire_date.setDate(emp.hire_date)

        if emp.gender == 1:
            self.rb_male.setChecked(True)
        else:
            self.rb_female.setChecked(True)
        self.cb_dept.clear()
        self.cb_dept.addItems([dept.dept_name for dept in self.dept_list])
        [self.cb_dept.setCurrentText(dept.dept_name) for dept in self.dept_list if emp.dept == dept.dept_no]
        [self.cb_manager.setCurrentText('{}({})'.format(manager.emp_name, manager.emp_no)) for manager in self.mgn_list_by_dept if emp.manager == manager.emp_no]
        [self.cb_title.setCurrentText(title.title_name) for title in self.title_list if emp.title == title.title_no]

        emp_pic = QPixmap()
        if emp.pic == 1:
            emp = EmployeeDao.instance().select_pic_by_empno(dto=emp)[0]
            emp_pic.loadFromData(emp.pic)
        else:
            emp_pic = QPixmap('no_img.png')
        self.lbl_img.setPixmap(emp_pic.scaled(150, 275, Qt.KeepAspectRatio))

    def clear_line_edit(self):
        self.le_no.setText('')
        self.le_name.setText('')
        self.sp_salary.setValue(1500000)
        self.le_pass1.setText('')
        self.le_pass2.setText('')
        self.lbl_pass_confirm.setText('')
        self.de_hire_date.setDate(QDate.currentDate())
        self.rb_male.setChecked(True)
        self.cb_dept.clear()
        self.cb_dept.addItems([dept.dept_name for dept in self.dept_list])
        self.cb_dept.setCurrentIndex(-1)
        self.cb_manager.clear()
        self.cb_manager.setCurrentIndex(-1)
        self.cb_title.setCurrentIndex(-1)
        pixmap = QPixmap('no_img.png')
        self.lbl_img.setPixmap(pixmap.scaled(150, 275, Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication([])
    window = EmployeeContentWidget()
    window.show()
    app.exec()