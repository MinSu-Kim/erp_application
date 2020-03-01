import logging
from abc import ABCMeta, abstractmethod

from connection.db_pool import DatabasePool


def iter_row(cursor, size=5):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


class Dao(metaclass=ABCMeta):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def insert_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def update_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def delete_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def select_item(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def get_dto(self, dto):
        raise NotImplementedError("Subclass must implement abstract method")

    def do_query(self, **kwargs):
        self.logger.info("do_query %s", kwargs)
        try:
            with DatabasePool.instance() as conn:
                with conn.cursor() as cursor:
                    if 'select' in kwargs['query'].lower():
                        cursor.execute(kwargs['query']) if kwargs['kargs'] is None else cursor.execute(kwargs['query'], kwargs['kargs'])
                        res = [self.get_dto(**row) for row in iter_row(cursor, 5)]
                    else:
                        cursor.execute(kwargs['query']) if kwargs['kargs'] is None else cursor.execute(kwargs['query'], kwargs['kargs'])
                        conn.commit()
                        res = f"{cursor.rowcount} rows affected."
                        self.logger.info(res)
            return res
        except Exception as err:
            self.logger.error(err)
