from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from .ui.main import Ui_MainWindow
from .add_book import AddBooxWindow
from cp.models.biblioteca import Biblioteca


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.__library = Biblioteca()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addBookButton.clicked.connect(self.add_book)

    @Slot()
    def add_book(self):
        wnd = AddBooxWindow(self.__library, self)
        wnd.show()
        wnd.exec()
        print("End")
