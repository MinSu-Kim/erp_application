import json
import logging.config

import pkg_resources

from connection.db_pool import DatabasePool
from dao.title_dao import TitleDao
from dto.dto_title import Title

if __name__ == "__main__":
    config = json.load(open(pkg_resources.resource_filename('resources', 'logger.json')))
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    with DatabasePool.instance() as conn:
        logger.info('%s conn', conn)

    # res = TitleDao.instance().select_item(
    #     sql='select title_no, title_name from title where title_no = %s',
    #     dto=Title(**{'title_no': 1, 'title_name': '사장'}))
    # logger.info('res type %s result %s', type(res), res)
    #
    # titles = TitleDao.instance().select_item()
    # logger.info('title list %s', titles)