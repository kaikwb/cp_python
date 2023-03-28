# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_bookQHYfxc.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_AddBook(object):
    def setupUi(self, AddBook):
        if not AddBook.objectName():
            AddBook.setObjectName(u"AddBook")
        AddBook.resize(263, 270)
        self.gridLayout_2 = QGridLayout(AddBook)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.titleLabel = QLabel(AddBook)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setLayoutDirection(Qt.LeftToRight)
        self.titleLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.titleLabel)

        self.titleEdit = QLineEdit(AddBook)
        self.titleEdit.setObjectName(u"titleEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.titleEdit)

        self.authorLable = QLabel(AddBook)
        self.authorLable.setObjectName(u"authorLable")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.authorLable)

        self.authorEdit = QLineEdit(AddBook)
        self.authorEdit.setObjectName(u"authorEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.authorEdit)

        self.isbnLabel = QLabel(AddBook)
        self.isbnLabel.setObjectName(u"isbnLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.isbnLabel)

        self.isbnEdit = QLineEdit(AddBook)
        self.isbnEdit.setObjectName(u"isbnEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.isbnEdit)

        self.yearLabel = QLabel(AddBook)
        self.yearLabel.setObjectName(u"yearLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.yearLabel)

        self.yearEdit = QLineEdit(AddBook)
        self.yearEdit.setObjectName(u"yearEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.yearEdit)

        self.availableLabel = QLabel(AddBook)
        self.availableLabel.setObjectName(u"availableLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.availableLabel)

        self.rareBookLabel = QLabel(AddBook)
        self.rareBookLabel.setObjectName(u"rareBookLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rareBookLabel)

        self.editionLabel = QLabel(AddBook)
        self.editionLabel.setObjectName(u"editionLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.editionLabel)

        self.editionEdit = QLineEdit(AddBook)
        self.editionEdit.setObjectName(u"editionEdit")
        self.editionEdit.setEnabled(True)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.editionEdit)

        self.stateLabel = QLabel(AddBook)
        self.stateLabel.setObjectName(u"stateLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.stateLabel)

        self.stateEdit = QLineEdit(AddBook)
        self.stateEdit.setObjectName(u"stateEdit")
        self.stateEdit.setEnabled(True)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.stateEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.isAvailableCheckBox = QCheckBox(AddBook)
        self.isAvailableCheckBox.setObjectName(u"isAvailableCheckBox")
        self.isAvailableCheckBox.setLayoutDirection(Qt.LeftToRight)
        self.isAvailableCheckBox.setAutoFillBackground(False)
        self.isAvailableCheckBox.setStyleSheet(u"")
        self.isAvailableCheckBox.setIconSize(QSize(0, 0))
        self.isAvailableCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.isAvailableCheckBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.isRareBookCheckBox = QCheckBox(AddBook)
        self.isRareBookCheckBox.setObjectName(u"isRareBookCheckBox")

        self.horizontalLayout_2.addWidget(self.isRareBookCheckBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.formLayout.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_2)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(AddBook)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(AddBook)
        self.buttonBox.accepted.connect(AddBook.accept)
        self.buttonBox.rejected.connect(AddBook.reject)

        QMetaObject.connectSlotsByName(AddBook)
    # setupUi

    def retranslateUi(self, AddBook):
        AddBook.setWindowTitle(QCoreApplication.translate("AddBook", u"Adicionar Livro", None))
        self.titleLabel.setText(QCoreApplication.translate("AddBook", u"T\u00edtulo:", None))
        self.authorLable.setText(QCoreApplication.translate("AddBook", u"Autor:", None))
        self.isbnLabel.setText(QCoreApplication.translate("AddBook", u"ISBN:", None))
        self.yearLabel.setText(QCoreApplication.translate("AddBook", u"Ano de publica\u00e7\u00e3o:", None))
        self.availableLabel.setText(QCoreApplication.translate("AddBook", u"Dispon\u00edvel:", None))
        self.rareBookLabel.setText(QCoreApplication.translate("AddBook", u"Livro raro:", None))
        self.editionLabel.setText(QCoreApplication.translate("AddBook", u"Edi\u00e7\u00e3o:", None))
        self.stateLabel.setText(QCoreApplication.translate("AddBook", u"Estado:", None))
        self.isAvailableCheckBox.setText("")
        self.isRareBookCheckBox.setText("")
    # retranslateUi

