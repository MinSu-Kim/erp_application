import imghdr
import inspect
import logging
import os

from pymysql import IntegrityError

from dao.abs_dao import Dao
from dto.dto_dept import Department
from dto.dto_emp import Employee
from util.singleton_instance import SingleTonInstance


class EmployeeDao(Dao, SingleTonInstance):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def insert_item(self, sql='insert into employee(emp_no, emp_name, gender, dept, manager, salary, title, hire_date, pic, pass) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, password(%s))', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        print(dto.get_to_dict())
        print(dto)
        return self.do_query(query=sql, kargs=tuple(dto))

    def update_item(self, sql='UPDATE employee SET emp_name=%s, gender=%s, dept=%s, manager=%s, salary=%s, title=%s, hire_date=%s, pass=password(%s), pic=%s WHERE emp_no=%s', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = dto.emp_name, dto.gender, dto.dept, dto.manager, dto.salary, dto.title, dto.hire_date, dto.passwd, dto.pic, dto.emp_no
        return self.do_query(query=sql, kargs=t)

    def delete_item(self, sql='delete from employee where emp_no=%s', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.emp_no,)
        return self.do_query(query=sql, kargs=t)

    def select_item(self, sql='select emp_no, emp_name, title, manager, salary, dept, hire_date, gender, if (pic is not null, 1, 0) as pic from employee', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        if dto is not None:
            if isinstance(dto, Employee):
                t = (dto.emp_no,)
            if isinstance(dto, Department):
                t = (dto.dept_no,)
        return self.do_query(query=sql, kargs=t if dto is not None else None)

    def select_pic_by_empno(self, sql='select pic from employee where emp_no = %s', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.emp_no,)
        return self.do_query(query=sql, kargs=t)

    def get_dto(self, **args):
        return Employee(**args)


def read_file(filename):
    with open(filename, 'rb') as f:
        photo = f.read()
    return photo


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)
    file_ext = imghdr.what(filename)
    os.rename(filename, filename+'.'+file_ext)
    return str(filename+'.'+file_ext)


if __name__ == "__main__":
    import json
    import logging.config
    import pkg_resources

    data = read_file(os.path.abspath(pkg_resources.resource_filename('images', '1003.jpeg')))
    config = json.load(open(pkg_resources.resource_filename('resources', 'logger.json')))
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    try:
        logger.info(EmployeeDao.instance().select_item())

        emp = Employee(emp_no = 1003)
        res = EmployeeDao.instance().select_pic_by_empno(dto=emp)
        logger.info(res)

        emp = Employee(emp_no = 1004, emp_name = '서현진', gender= False, dept= 1, manager = 4377, salary = 4000000, title = 2, hire_date = '2000-02-11', passwd = '1234')
        logger.info(emp)
        res = EmployeeDao.instance().insert_item(dto=emp)
        logger.info(res)

        emp.emp_name = '수지'
        emp.gender = False
        emp.dept = 3
        emp.manager = 1003
        emp.salary = 2000000
        emp.title = 3
        emp.hire_date = '2001-02-11'
        emp.passwd = '2222'

        emp.pic = data
        res = EmployeeDao.instance().update_item(dto=emp)
        logger.info(res)

        logger.info(EmployeeDao.instance().select_item())

        res = EmployeeDao.instance().delete_item(dto=emp)
        logger.info(res)
    except IntegrityError as e:
        print(e)

