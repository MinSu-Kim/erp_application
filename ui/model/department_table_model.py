from PyQt5.QtCore import QVariant, Qt

from ui.model.abstract_table_model import AbstractTableModel


class DepartmentTableModel(AbstractTableModel):

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.TextAlignmentRole:
            if index.column() in [0, 1, 2] :
                return Qt.AlignCenter
        if role != Qt.DisplayRole:
            return QVariant()
        return self.data[index.row()][index.column()]