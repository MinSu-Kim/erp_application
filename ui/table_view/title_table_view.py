import inspect
import logging

from PyQt5.QtWidgets import QApplication

from dao.title_dao import TitleDao
from dto.dto_title import Title
from ui.model.title_table_model import TitleTableModel
from ui.table_view.abstract_table_view import AbstractTableViewWidget


class TitleTableViewWidget(AbstractTableViewWidget):
    def __init__(self, parent=None):
        super(TitleTableViewWidget, self).__init__(parent)
        self.table_header = ['직책 코드', '직책 명']
        self.table_data = [tuple(title) for title in TitleDao.instance().select_item()]
        self.model = TitleTableModel(data=self.table_data, header=self.table_header)
        self.tableView.setModel(self.model)

    # def get_model(self):
    #     return TitleTableModel(data=self.table_data, header=self.table_header)
    #
    # def get_data(self):
    #     return [tuple(title) for title in TitleDao.instance().select_item()]
    #
    # def get_header(self):
    #     return ['직책 코드', '직책 명']

    def get_column_size(self):
        return 100, 100

    def get_dto(self, tuple_item):
        self.logger.info("\n{}({})".format(inspect.stack()[0][3], tuple_item))
        title = Title()
        title.title_no = tuple_item[0]
        title.title_name = tuple_item[1]
        return title


if __name__ == '__main__':
    import json
    import logging.config
    import pkg_resources

    config = json.load(open(pkg_resources.resource_filename('resources', 'logger.json')))
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    app = QApplication([])
    # d = DepartmentTableViewWidget()
    t = TitleTableViewWidget()
    t.show()
    app.exec()