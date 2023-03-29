from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from PySide6.QtCore import Slot, QAbstractTableModel, QModelIndex
from .ui.main import Ui_MainWindow
from .add_book import AddBooxWindow
from cp.models.biblioteca import Biblioteca

from cp.models.livro_raro import LivroRaro

from cp.models.book_table import BookTableModel

from PySide6.QtCore import Qt

from typing import List

#
# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data, headers):
#         super().__init__()
#         self._data = data
#         self._headers = headers
#
#     def rowCount(self, parent=QModelIndex()):
#         return len(self._data)
#
#     def columnCount(self, parent=QModelIndex()):
#         return len(self._headers)
#
#     def data(self, index, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole or role == Qt.EditRole:
#             return self._data[index.row()][index.column()]
#         elif role == Qt.CheckStateRole and index.column() == 0:
#             return Qt.Checked if self._data[index.row()][index.column()] else Qt.Unchecked
#
#     def setData(self, index, value, role=Qt.EditRole):
#         if role == Qt.CheckStateRole and index.column() == 0:
#             self._data[index.row()][index.column()] = value == Qt.Checked
#             self.dataChanged.emit(index, index)
#             return True
#         elif role == Qt.EditRole:
#             self._data[index.row()][index.column()] = value
#             self.dataChanged.emit(index, index)
#             return True
#         return False
#
#     def flags(self, index):
#         if index.column() == 0:
#             return Qt.ItemIsUserCheckable | super().flags(index)
#         return super().flags(index)
#
#     def headerData(self, section, orientation, role=Qt.DisplayRole):
#         if role == Qt.DisplayRole and orientation == Qt.Horizontal:
#             return self._headers[section]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__library = Biblioteca()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__table_model = BookTableModel([])
        self.ui.booksTableView.setModel(self.__table_model)
        self.__table_model.fill_books([LivroRaro("a", "b", "1234", 2022, 1, "ruim", True)])

        self.ui.removeBookButton.setEnabled(False)
        self.ui.borrowBookButton.setEnabled(False)
        self.ui.returnBookButton.setEnabled(False)

        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.listBooksButton.clicked.connect(self.list_all_books)

    def __fill_list_table(self, books: List):
        table = self.ui.booksTableWidget
        # table.clearContents()
        # table.setRowCount(len(books))
        #
        # for i, book in enumerate(books):
        #     title = self.__create_table_cell(book.titulo)
        #     author = self.__create_table_cell(book.autor)
        #     isbn = self.__create_table_cell(book.isbn)
        #     year = self.__create_table_cell(str(book.ano_publicacao))
        #     is_available = self.__create_table_cell("", is_bool=True)
        #
        #     table.setItem(i, 0, title)
        #     table.setItem(i, 1, author)
        #     table.setItem(i, 2, isbn)
        #     table.setItem(i, 3, year)
        #     table.setItem(i, 4, is_available)

    @Slot()
    def add_book(self):
        wnd = AddBooxWindow(self.__library, self)
        wnd.show()
        wnd.exec()
        print("End")

    @Slot()
    def list_all_books(self):
        books = self.__library.listar_livros()
        self.__fill_list_table(books)
