from typing import List

from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

from cp.models.livro import Livro
from cp.models.livro_raro import LivroRaro


class BookTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        if data is None:
            data = list()
        self.__data = list()
        self.__data_obj = data
        self.__headers = ["Disponível", "Título", "Autor", "ISBN", "Ano", "Raro", "Edição", "Estado"]
        self.__bool_columns = [0, 5]

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.__data)

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self.__headers)

    def data(self, index: QModelIndex, role=Qt.DisplayRole) -> str | Qt.CheckState:
        row = index.row()
        col = index.column()
        if (role == Qt.DisplayRole or role == Qt.EditRole) and (col not in self.__bool_columns):
            return self.__data[row][col]
        elif role == Qt.ItemDataRole.CheckStateRole and (col in self.__bool_columns):
            return Qt.CheckState.Checked if self.__data[row][col] else Qt.CheckState.Unchecked

    def setData(self, index: QModelIndex, value: str | bool, role=Qt.ItemDataRole.EditRole) -> bool:
        if role == Qt.ItemDataRole.EditRole:
            self.__data[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index: QModelIndex) -> int:
        idx_flags = Qt.ItemIsEnabled | super().flags(index)
        if index in self.__bool_columns:
            idx_flags |= Qt.ItemDataRole.CheckStateRole
        return idx_flags

    def headerData(self, section: int, orientation: Qt.Orientation, role=Qt.DisplayRole) -> str:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.__headers[section]

    def insertRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        self.beginInsertRows(parent, row, row + count - 1)
        for i in range(count):
            self.__data.insert(row + i, [None] * self.columnCount())
        self.endInsertRows()
        return True

    def removeRows(self, row: int, count: int, parent=QModelIndex()) -> bool:
        self.beginRemoveRows(parent, row, row + count - 1)
        del self.__data[row:row + count]
        self.endRemoveRows()
        return True

    def clear(self) -> None:
        self.removeRows(0, self.rowCount())
        self.__data_obj = None

    def fill_books(self, books: List[Livro | LivroRaro]) -> None:
        self.clear()
        self.insertRows(0, len(books))
        for i, book in enumerate(books):
            idx = self.index(i, 0)
            self.__set_line_content(idx, book)
        self.__data_obj = books

    def get_book(self, index: int) -> Livro:
        return self.__data_obj[index]

    def redraw_items(self) -> None:
        self.fill_books(self.__data_obj)

    def __set_line_content(self, idx: QModelIndex, book: Livro | LivroRaro) -> None:
        is_rare = issubclass(type(book), LivroRaro)
        value = [
            book.disponivel,
            book.titulo,
            book.isbn,
            book.autor,
            book.ano_publicacao,
            is_rare,
            book.edicao if is_rare else "",
            book.estado if is_rare else ""
        ]
        self.setData(idx, value)
