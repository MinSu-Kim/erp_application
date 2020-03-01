import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

from dto.dto_title import Title


class TitleContent(QWidget):

    def __init__(self, parent=None):
        super(TitleContent, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/content_title.ui')
        self.ui = uic.loadUi(ui_path, self)
        self.le_no = self.ui.le_no
        self.le_name = self.ui.le_name

    def get_item(self):
        try:
            title_name = self.le_name.text()
            title_no = self.le_no.text()
            return Title(title_no, title_name);
        except Exception as err:
            print(err)

    def set_item(self, title):
        self.le_no.setText(str(title.title_no))
        self.le_name.setText(title.title_name)

    def clear_line_edit(self):
        self.le_no.setText('')
        self.le_name.setText('')


if __name__ == "__main__":
    app = QApplication([])
    w = TitleContent()
    w.show()
    sys.exit(app.exec_())