from .livro import Livro


class LivroComum(Livro):
    def __init__(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, disponivel: bool):
        super().__init__(titulo, autor, isbn, ano_publicacao, disponivel)
