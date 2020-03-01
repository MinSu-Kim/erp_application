import json
import logging.config

import pkg_resources
from pymysqlpool.pool import Pool

from util.singleton_instance import SingleTonInstance


class DatabasePool(SingleTonInstance):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.__cnxPool = Pool(host='localhost', port=3306, user='user_pyqt_erp_proj', password='rootroot', db='pyqt_erp_proj')
        self.__cnxPool.init()

    def __enter__(self):
        self.logger.debug('__enter__')
        self.conn = self.__cnxPool.get_conn()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.debug('__enter__')
        self.__cnxPool.release(self.conn)


if __name__ == "__main__":
    config = json.load(open(pkg_resources.resource_filename('resources', 'logger.json')))
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    try:
        with DatabasePool.instance() as conn:
            logger.info('conn = %s', conn)
    except Exception as err:
        logger.error(err)
