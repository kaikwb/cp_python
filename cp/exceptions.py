from cp.models.livro import Livro


class BookAlreadyRegistred(Exception):
    def __init__(self, book: Livro):
        super().__init__(f"O livro [{book}] já registrado")


class BookAlreadyBorrowed(Exception):
    def __init__(self, book: Livro):
        super().__init__(f"O livro [{book}] já emprestado")


class BookNotBorrowed(Exception):
    def __init__(self, book: Livro):
        super().__init__(f"O livro [{book}] não está emprestado")


class BookNotFound(Exception):
    def __init__(self, attribute, value):
        super().__init__(f"O livro com {attribute} igual a [{value}] não foi encontrado")
