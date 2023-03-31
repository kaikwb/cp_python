from typing import Optional, List

from cp.exceptions import BookAlreadyRegistred, BookAlreadyBorrowed, BookNotBorrowed
from cp.utils import fuzzy_search, title_processor, author_processor, isbn_processor
from .livro import Livro


class Biblioteca(object):
    def __init__(self):
        self.__books = list()

    @property
    def livros(self) -> List[Livro]:
        return self.__books

    def adicionar_livro(self, livro: Livro) -> None:
        for book in filter(lambda x: x.isbn == livro.isbn, self.livros):
            raise BookAlreadyRegistred(book)
        else:
            self.__books.append(livro)

    def remover_livro(self, livro: Livro) -> None:
        self.__books.remove(livro)

    def buscar_livro_por_titulo(self, titulo: str) -> Optional[Livro]:
        for book in filter(lambda x: x.titulo == titulo, self.livros):
            return book
        else:
            return None

    def buscar_livro_por_autor(self, autor: str) -> List[Livro]:
        return list(filter(lambda x: x.autor == autor, self.livros))

    def buscar_livro_por_isbn(self, isbn: str) -> Optional[Livro]:
        for book in filter(lambda x: x.isbn == isbn, self.livros):
            return book
        else:
            return None

    def busca_nebulosa(self, search_text: str, search_type: str) -> List[Livro]:
        match search_type:
            case "Título":
                processor = title_processor
            case "Autor":
                processor = author_processor
            case "ISBN":
                processor = isbn_processor
            case _:
                processor = title_processor

        return fuzzy_search(search_text, self.livros, processor=processor)

    def listar_livros(self) -> List[Livro]:
        return self.livros

    @staticmethod
    def registrar_emprestimo(livro: Livro) -> None:
        if livro.disponivel:
            livro.emprestar()
        else:
            raise BookAlreadyBorrowed(livro)

    @staticmethod
    def registrar_devolucao(livro: Livro) -> None:
        if livro.disponivel:
            raise BookNotBorrowed(livro)
        else:
            livro.devolver()

    def listar_livros_emprestados(self) -> List[Livro]:
        return list(filter(lambda x: not x.disponivel, self.livros))
