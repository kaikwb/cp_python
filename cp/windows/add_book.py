from typing import Dict

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtWidgets import QWidget

from cp.exceptions import BookAlreadyRegistred
from cp.models.biblioteca import Biblioteca
from cp.models.livro import Livro
from cp.models.livro_comum import LivroComum
from cp.models.livro_raro import LivroRaro
from cp.windows.ui.add_book import Ui_AddBook


class AddBooxWindow(QDialog):
    def __init__(self, library: Biblioteca, parent: QWidget = None):
        super().__init__(parent=parent)

        self.__library = library

        self.ui = Ui_AddBook()
        self.ui.setupUi(self)

    def __get_book_attributes(self) -> Dict[str, str | bool]:
        attr = dict()

        attr["title"] = self.ui.titleEdit.text()
        attr["author"] = self.ui.authorEdit.text()
        attr["isbn"] = self.ui.isbnEdit.text()
        attr["year"] = self.ui.yearEdit.text()
        attr["is_available"] = self.ui.isAvailableCheckBox.isChecked()
        attr["is_rare"] = self.ui.isRareBookCheckBox.isChecked()
        attr["edition"] = self.ui.editionEdit.text()
        attr["state"] = self.ui.editionEdit.text()

        return attr

    @staticmethod
    def __create_book_from_attributes(attr: Dict[str, str | bool]) -> Livro:
        if attr["is_rare"]:
            book = LivroRaro(
                attr["title"],
                attr["author"],
                attr["isbn"],
                attr["year"],
                attr["edition"],
                attr["state"],
                attr["is_available"]
            )
        else:
            book = LivroComum(
                attr["title"],
                attr["author"],
                attr["isbn"],
                attr["year"],
                attr["is_available"]
            )

        return book

    def __show_success_message(self) -> None:
        QMessageBox.information(self, "Adicionar Livro", "Livro Adicionado com sucesso.", QMessageBox.StandardButton.Ok)

    def __show_fail_message(self, isbn: str) -> None:
        QMessageBox.critical(self, "Adicionar Livro", f"Livro com ISBN {isbn} já cadastrado.",
                             QMessageBox.StandardButton.Ok)

    def __add_book_to_library(self) -> None:
        attr = self.__get_book_attributes()
        book = self.__create_book_from_attributes(attr)

        try:
            self.__library.adicionar_livro(book)
            self.__show_success_message()
        except BookAlreadyRegistred:
            self.__show_fail_message(attr["isbn"])

    @Slot()
    def accept(self) -> None:
        self.__add_book_to_library()
        self.close()
