import inspect
import logging.config

from pymysql import IntegrityError

from dao.abs_dao import Dao
from dto.dto_title import Title
from util.singleton_instance import SingleTonInstance


class TitleDao(Dao, SingleTonInstance):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def insert_item(self, sql='insert into title values(%s, %s)', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        return self.do_query(query=sql, kargs=tuple(dto))

    def update_item(self, sql='UPDATE title SET title_name=%s WHERE title_no=%s', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.title_name, dto.title_no)
        return self.do_query(query=sql, kargs=t)

    def delete_item(self, sql='DELETE FROM title WHERE title_no=%s', dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        t = (dto.title_no,)
        return self.do_query(query=sql, kargs=t)

    def select_item(self, sql="select title_no, title_name from title", dto=None):
        self.logger.info("\n{}() {} {}".format(inspect.stack()[0][3], sql, dto, end=' => '))
        if dto is not None:
            t = (dto.title_no,)
        return self.do_query(query=sql, kargs=t if dto is not None else None)

    def get_dto(self, **args):
        return Title(**args)


if __name__ == "__main__":
    import json
    import logging.config
    import pkg_resources

    config = json.load(open(pkg_resources.resource_filename('resources', 'logger.json')))
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    try:
        res = TitleDao.instance().select_item(
            sql='select title_no, title_name from title where title_no = %s',
            dto=Title(**{'title_no': 1, 'title_name': '사장'}))
        logger.info('res type %s result %s', type(res), res)

        titles = TitleDao.instance().select_item()
        logger.info('title list %s', titles)

        title_intern = Title(6, '인턴')
        res = TitleDao.instance().insert_item(dto=title_intern)
        logger.info('res : %s', res)

        title_intern.title_name = '계약직'
        res = TitleDao.instance().update_item(dto=title_intern)
        logger.info('res : %s', res)

        res = TitleDao.instance().delete_item(dto=title_intern)
        logger.info('res : %s', res)
    except IntegrityError as e:
        logger.error(e)
