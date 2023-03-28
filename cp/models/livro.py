class Livro(object):
    def __init__(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, disponivel: bool):
        super().__init__()
        self.a = 5
        self.__title = titulo
        self.__author = autor
        self.__isbn = isbn
        self.__year = ano_publicacao
        self.__available = disponivel

    def __str__(self):
        return f"{self.autor} - {self.titulo} ({self.ano_publicacao}) - ISDB:{self.isbn} [{self.disponivel}]"

    @property
    def titulo(self) -> str:
        return self.__title

    @property
    def autor(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def ano_publicacao(self) -> int:
        return self.__year

    @property
    def disponivel(self) -> bool:
        return self.__available

    def emprestar(self):
        self.__available = False

    def devolver(self):
        self.__available = True
