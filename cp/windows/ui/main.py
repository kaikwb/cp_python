# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUaVRfy.ui'
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
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(669, 274)
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

        self.booksTableWidget = QTableWidget(self.centralwidget)
        if (self.booksTableWidget.columnCount() < 8):
            self.booksTableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.booksTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.booksTableWidget.setObjectName(u"booksTableWidget")

        self.verticalLayout.addWidget(self.booksTableWidget)

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

        ___qtablewidgetitem = self.booksTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem1 = self.booksTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem2 = self.booksTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ISBN", None));
        ___qtablewidgetitem3 = self.booksTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        ___qtablewidgetitem4 = self.booksTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Dispon\u00edvel", None));
        ___qtablewidgetitem5 = self.booksTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Raro", None));
        ___qtablewidgetitem6 = self.booksTableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Edi\u00e7\u00e3o", None));
        ___qtablewidgetitem7 = self.booksTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        self.addBookButton.setText(QCoreApplication.translate("MainWindow", u"Adicionar Livro", None))
        self.removeBookButton.setText(QCoreApplication.translate("MainWindow", u"Remover Livro", None))
        self.listBooksButton.setText(QCoreApplication.translate("MainWindow", u"Listar Todos os Livros", None))
        self.borrowBookButton.setText(QCoreApplication.translate("MainWindow", u"Emprestar Livro", None))
        self.returnBookButton.setText(QCoreApplication.translate("MainWindow", u"Devolver Livro", None))
    # retranslateUi
