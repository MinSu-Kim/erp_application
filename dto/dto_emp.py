from dto.dto_dept import Department
from dto.dto_title import Title


class Employee():
    def __init__(self, emp_no=None, emp_name=None, title=None, manager=None, salary=None, dept=None, hire_date=None, gender=None, passwd=None, pic=None):
        # emp_no, emp_name, title, manager, salary, dept, hire_date, gender, passwd, pic
        self.__emp_no = emp_no
        self.__emp_name = emp_name
        self.__title = title
        self.__manager = manager
        self.__salary = salary
        self.__dept = dept
        self.__hire_date = hire_date
        self.__passwd = passwd
        self.__gender = gender
        self.__pic = pic

    @property
    def emp_no(self):
        return self.__emp_no

    @emp_no.setter
    def emp_no(self, emp_no):
        self.__emp_no = emp_no

    @property
    def emp_name(self):
        return self.__emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        self.__emp_name = emp_name

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def dept(self):
        return self.__dept

    @dept.setter
    def dept(self, dept):
        self.__dept = dept;

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, manager):
        self.__manager = manager

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def hire_date(self):
        return self.__hire_date

    @hire_date.setter
    def hire_date(self, hire_date):
        self.__hire_date = hire_date

    @property
    def passwd(self):
        return self.__passwd

    @passwd.setter
    def passwd(self, passwd):
        self.__passwd = passwd

    @property
    def pic(self):
        return self.__pic

    @pic.setter
    def pic(self, pic):
        self.__pic = pic

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __iter__(self):
        # emp_no, emp_name, gender, dept, manager, salary, title, hire_date, password
        return (i for i in (self.__emp_no, self.__emp_name, self.__gender, self.__dept, self.__manager, self.__salary, self.__title, self.__hire_date, self.__pic, self.__passwd))

    def __repr__(self) -> str:
        return '{}({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            type(self).__name__, self.__emp_no, self.__emp_name, self.__gender, self.__dept, self.__manager, self.__salary, self.__title, self.__hire_date, self.__pic, self.__passwd)

    def __hash__(self):
        return hash(self.__emp_no) ^ hash(self.__emp_name)

    def get_to_dict(self):
        return {
            'emp_no': self.__emp_no,
            'emp_name': self.__emp_name,
            'gender': self.__gender,
            'dept': self.__dept,
            'manager': self.__manager,
            'salary': self.__salary,
            'title': self.__title,
            'hire_date': self.__hire_date,
            'pic': self.__pic,
            'passwd':self.__passwd
        }


if __name__ == "__main__":
    kargs = {'emp_no': 1, 'emp_name': '김민수', 'gender': True, 'dept': Department(dept_no=1),
             'manager': Employee(**{'emp_no': 1}),
             'salary': 1500000, 'title': Title(title_no=1), 'hire_date': '2020-02-18',
             'passwd':'1234'}
    [print(k, end=', ') for k, v in kargs.items()]
    empList = [Employee(**kargs), Employee(**kargs)]

    empList.append(Employee(**{'emp_no':2}))
    [print(e.get_to_dict()) for e in empList]

    print(empList[0] == empList[1])

    print(Employee(**{'emp_no': 1, 'emp_name': '김민수'}).get_to_dict())

    print(tuple(empList[1]))

