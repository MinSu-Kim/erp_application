from PyQt5.QtCore import QVariant, Qt, QAbstractTableModel


class TitleTableModel(QAbstractTableModel):
    def __init__(self, data=None, header=None, parent=None):
        super(TitleTableModel, self).__init__(parent)
        self.data = data or [()]
        self.header = header or [()]

    def rowCount(self, parent):
        return len(self.data)

    def columnCount(self, parent):
        return len(self.data[0])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[col])
        return QVariant()

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.TextAlignmentRole:
            if index.column() in [0, 1]:
                return Qt.AlignCenter
        if role != Qt.DisplayRole:
            return QVariant()
        return self.data[index.row()][index.column()]