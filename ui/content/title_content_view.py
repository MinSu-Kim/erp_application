from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import *

from dto.dto_title import Title


class TitleContentWidget(QWidget):
    def __init__(self, parent=None):
        super(TitleContentWidget, self).__init__(parent)
        root_layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(root_layout)
        self.init_component(root_layout)

    def init_component(self, root_layout):
        item_size = QSize(0, 40)
        self.lbl_no = QLabel('직책번호', self)
        self.lbl_no.setAlignment(Qt.AlignCenter)
        self.lbl_no.setMinimumSize(item_size)
        self.lbl_name = QLabel('직책명', self)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.lbl_name.setMinimumSize(item_size)

        self.le_no = QLineEdit()
        self.le_no.setMinimumSize(item_size)
        self.le_name = QLineEdit()
        self.le_name.setMinimumSize(item_size)

        echo_group = QGroupBox('직책', self)
        group_layout = QGridLayout()
        echo_group.setLayout(group_layout)
        group_layout.addWidget(self.lbl_no, 0, 0, 1, 1)
        group_layout.addWidget(self.le_no, 0, 1, 1, 1)
        group_layout.addWidget(self.lbl_name, 1, 0, 1, 1)
        group_layout.addWidget(self.le_name, 1, 1, 1, 1)
        root_layout.addWidget(echo_group)

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


if __name__ == '__main__':
    app = QApplication([])
    t = TitleContentWidget()
    t.show()
    app.exec()
