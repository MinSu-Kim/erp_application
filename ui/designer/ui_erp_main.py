import sys

import pkg_resources
from PyQt5 import uic
from PyQt5.QtWidgets import *


class ERP(QMainWindow):

    def __init__(self, parent=None):
        super(ERP, self).__init__(parent)
        ui_path = pkg_resources.resource_filename('ui', 'designer/erp_main.ui')
        self.ui = uic.loadUi(ui_path, self)


if __name__ == "__main__":
    app = QApplication([])
    w = ERP()
    w.show()
    sys.exit(app.exec_())