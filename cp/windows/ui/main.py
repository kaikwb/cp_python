# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainnWlopn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 274)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchLabel = QLabel(self.centralwidget)
        self.searchLabel.setObjectName(u"searchLabel")

        self.horizontalLayout.addWidget(self.searchLabel)

        self.searchEdit = QLineEdit(self.centralwidget)
        self.searchEdit.setObjectName(u"searchEdit")

        self.horizontalLayout.addWidget(self.searchEdit)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout.addWidget(self.searchButton)

        self.fuzzyCheckBox = QCheckBox(self.centralwidget)
        self.fuzzyCheckBox.setObjectName(u"fuzzyCheckBox")

        self.horizontalLayout.addWidget(self.fuzzyCheckBox)

        self.searchComboBox = QComboBox(self.centralwidget)
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.searchComboBox.addItem("")
        self.searchComboBox.setObjectName(u"searchComboBox")
        self.searchComboBox.setMinimumSize(QSize(120, 0))

        self.horizontalLayout.addWidget(self.searchComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.booksTableView = QTableView(self.centralwidget)
        self.booksTableView.setObjectName(u"booksTableView")

        self.verticalLayout.addWidget(self.booksTableView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.addBookButton = QPushButton(self.centralwidget)
        self.addBookButton.setObjectName(u"addBookButton")
        self.addBookButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.addBookButton)

        self.removeBookButton = QPushButton(self.centralwidget)
        self.removeBookButton.setObjectName(u"removeBookButton")
        self.removeBookButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.removeBookButton)

        self.listBooksButton = QPushButton(self.centralwidget)
        self.listBooksButton.setObjectName(u"listBooksButton")
        self.listBooksButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.listBooksButton)

        self.borrowBookButton = QPushButton(self.centralwidget)
        self.borrowBookButton.setObjectName(u"borrowBookButton")
        self.borrowBookButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.borrowBookButton)

        self.returnBookButton = QPushButton(self.centralwidget)
        self.returnBookButton.setObjectName(u"returnBookButton")
        self.returnBookButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.returnBookButton)

        self.listBorrowedButton = QPushButton(self.centralwidget)
        self.listBorrowedButton.setObjectName(u"listBorrowedButton")
        self.listBorrowedButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout_2.addWidget(self.listBorrowedButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Alexandria", None))
        self.searchLabel.setText(QCoreApplication.translate("MainWindow", u"Buscar por:", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.fuzzyCheckBox.setText(QCoreApplication.translate("MainWindow", u"Fuzzy Search", None))
        self.searchComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.searchComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Autor", None))
        self.searchComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"ISBN", None))

        self.addBookButton.setText(QCoreApplication.translate("MainWindow", u"Adicionar Livro", None))
        self.removeBookButton.setText(QCoreApplication.translate("MainWindow", u"Remover Livro", None))
        self.listBooksButton.setText(QCoreApplication.translate("MainWindow", u"Listar Todos os Livros", None))
        self.borrowBookButton.setText(QCoreApplication.translate("MainWindow", u"Emprestar Livro", None))
        self.returnBookButton.setText(QCoreApplication.translate("MainWindow", u"Devolver Livro", None))
        self.listBorrowedButton.setText(QCoreApplication.translate("MainWindow", u"Listar Livros Emprestados", None))
    # retranslateUi

