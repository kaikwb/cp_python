from collections.abc import Iterable
from typing import List

from PySide6.QtCore import Qt
from PySide6.QtCore import Slot, QModelIndex
from PySide6.QtWidgets import QMainWindow, QMessageBox

from cp.exceptions import BookAlreadyBorrowed, BookNotBorrowed, BookNotFound
from cp.models.biblioteca import Biblioteca
from cp.models.book_table import BookTableModel
from cp.models.livro import Livro
from .add_book import AddBooxWindow
from .ui.main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__library = Biblioteca()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.__table_model = BookTableModel(self.__library.listar_livros())
        self.ui.booksTableView.setModel(self.__table_model)

        self.enable_book_operations(False)

        self.ui.addBookButton.clicked.connect(self.add_book)
        self.ui.removeBookButton.clicked.connect(self.remove_book)
        self.ui.listBooksButton.clicked.connect(self.list_all_books)
        self.ui.borrowBookButton.clicked.connect(self.borrow_book)
        self.ui.returnBookButton.clicked.connect(self.return_book)
        self.ui.searchButton.clicked.connect(self.search_book)
        self.ui.listBorrowedButton.clicked.connect(self.list_borrowed_books)

        self.ui.booksTableView.selectionModel().currentRowChanged.connect(self.select_item)

        self.ui.searchEdit.textEdited.connect(self.search_on_change)
        self.ui.searchComboBox.currentTextChanged.connect(self.search_on_change)

    @Slot()
    def add_book(self) -> None:
        wnd = AddBooxWindow(self.__library, self)
        wnd.show()
        wnd.exec()
        self.__table_model.redraw_items()

    @Slot()
    def remove_book(self) -> None:
        book = self.get_selected_book()
        self.__library.remover_livro(book)
        self.__table_model.redraw_items()

    @Slot()
    def list_all_books(self) -> None:
        self.__table_model.fill_books(self.__library.listar_livros())

    @Slot()
    def list_borrowed_books(self) -> None:
        self.__table_model.fill_books(self.__library.listar_livros_emprestados())

    @Slot()
    def borrow_book(self) -> None:
        book = self.get_selected_book()

        try:
            self.__library.registrar_emprestimo(book)
            self.show_borrow_success_message()
        except BookAlreadyBorrowed:
            self.show_borrow_fail_message()

        self.__table_model.redraw_items()

    @Slot()
    def return_book(self) -> None:
        book = self.get_selected_book()

        try:
            self.__library.registrar_devolucao(book)
            self.show_return_success_message()
        except BookNotBorrowed:
            self.show_return_fail_message()

        self.__table_model.redraw_items()

    @Slot()
    def enable_book_operations(self, state) -> None:
        self.ui.removeBookButton.setEnabled(state)
        self.ui.borrowBookButton.setEnabled(state)
        self.ui.returnBookButton.setEnabled(state)

    @Slot(QModelIndex, QModelIndex)
    def select_item(self, selected: QModelIndex, deselected: QModelIndex) -> None:
        row = selected.row()
        self.enable_book_operations(True if row >= 0 else False)

    @Slot()
    def search_book(self) -> None:
        search_text = self.ui.searchEdit.text()
        search_type = self.ui.searchComboBox.currentText()

        if search_text == "":
            self.list_all_books()
        else:
            try:
                if self.is_fuzzy_search:
                    search_result = self.fuzzy_search(search_text, search_type)
                else:
                    search_result = self.fuzzy_search(search_text, search_type)
            except BookNotFound:
                search_result = list()
                self.show_search_fail_message()

            self.__table_model.fill_books(search_result)

    def search_single(self, search_text: str, search_type: str) -> List[Livro]:
        if search_type == "Título":
            search_result = self.__library.buscar_livro_por_titulo(search_text)
        elif search_type == "Autor":
            search_result = self.__library.buscar_livro_por_autor(search_text)
        else:
            search_result = self.__library.buscar_livro_por_isbn(search_text)

        if search_result is None:
            raise BookNotFound(search_type, search_text)
        else:
            return search_result if isinstance(search_result, Iterable) else [search_result]

    def fuzzy_search(self, search_text: str, search_type: str) -> List[Livro]:
        return self.__library.busca_nebulosa(search_text, search_type)

    @Slot()
    def search_on_change(self) -> None:
        if self.is_fuzzy_search:
            self.search_book()

    @property
    def is_fuzzy_search(self) -> bool:
        return self.ui.fuzzyCheckBox.checkState() == Qt.CheckState.Checked

    def get_selected_book(self) -> Livro:
        row = self.ui.booksTableView.selectionModel().currentIndex().row()
        book = self.__table_model.get_book(row)
        return book

    def show_borrow_success_message(self) -> None:
        QMessageBox.information(self, "Emprestar Livro", "Livro emprestado com sucesso.", QMessageBox.StandardButton.Ok)

    def show_borrow_fail_message(self) -> None:
        QMessageBox.critical(self, "Emprestar Livro", f"Livro já está emprestado.", QMessageBox.StandardButton.Ok)

    def show_return_success_message(self) -> None:
        QMessageBox.information(self, "Devolver Livro", "Livro devolvido com sucesso.", QMessageBox.StandardButton.Ok)

    def show_return_fail_message(self) -> None:
        QMessageBox.critical(self, "Devolver Livro", f"Livro não está emprestado.", QMessageBox.StandardButton.Ok)

    def show_search_fail_message(self) -> None:
        QMessageBox.critical(self, "Buscar Livro", f"Nenhum livro encontrado.", QMessageBox.StandardButton.Ok)
