from .livro import Livro


class LivroRaro(Livro):
    def __init__(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, edicao: int, estado: str,
                 disponivel: bool):
        super().__init__(titulo, autor, isbn, ano_publicacao, disponivel)
        self.__edition = edicao
        self.__state = estado

    def __str__(self) -> str:
        return f"{self.autor} - {self.titulo} ({self.ano_publicacao}) - ISDB:{self.isbn} [{self.disponivel}] - " \
               f"Edição: {self.edicao} - Estado: {self.estado}"

    @property
    def edicao(self) -> int:
        return self.__edition

    @property
    def estado(self) -> str:
        return self.__state
