class Livro(object):
    """
    É solicitado para implementar um método __dict__(self), porém __dict__ é um atributo que armazena o namespace
    da classe/objeto e não um método.

    Sobreescrever ele como método pode levar ao sistema apresentar comportamentos não esperados e não é recomendavel.

    Abaixo links para a documentação do Python que descrevem isso:
    https://docs.python.org/3/library/stdtypes.html#object.__dict__
    """

    def __init__(self, titulo: str, autor: str, isbn: str, ano_publicacao: int, disponivel: bool):
        super().__init__()
        self.a = 5
        self.__title = titulo
        self.__author = autor
        self.__isbn = isbn
        self.__year = ano_publicacao
        self.__available = disponivel

    def __str__(self) -> str:
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

    def emprestar(self) -> None:
        self.__available = False

    def devolver(self) -> None:
        self.__available = True
