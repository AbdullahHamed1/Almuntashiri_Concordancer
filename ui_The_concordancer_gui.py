# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'The_concordancer_guiMfinGf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)

from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 800)
        font = QFont()
        font.setPointSize(24)
        Form.setFont(font)
        Form.setLayoutDirection(Qt.RightToLeft)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_title = QLabel(Form)
        self.lb_title.setObjectName(u"lb_title")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(36)
        self.lb_title.setFont(font1)
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_title)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_root_1 = QLabel(Form)
        self.lb_root_1.setObjectName(u"lb_root_1")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(24)
        self.lb_root_1.setFont(font2)

        self.verticalLayout_2.addWidget(self.lb_root_1)

        self.lb_root = QLabel(Form)
        self.lb_root.setObjectName(u"lb_root")
        self.lb_root.setFont(font2)
        self.lb_root.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.lb_root)

        self.tb_result = QTableWidget(Form)
        if (self.tb_result.columnCount() < 2):
            self.tb_result.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tb_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tb_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_result.setObjectName(u"tb_result")
        self.tb_result.setFont(font2)
        self.tb_result.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tb_result)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_search = QPushButton(Form)
        self.bt_search.setObjectName(u"bt_search")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_search.sizePolicy().hasHeightForWidth())
        self.bt_search.setSizePolicy(sizePolicy)
        self.bt_search.setFont(font2)

        self.horizontalLayout.addWidget(self.bt_search)

        self.le_search = QLineEdit(Form)
        self.le_search.setObjectName(u"le_search")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_search.sizePolicy().hasHeightForWidth())
        self.le_search.setSizePolicy(sizePolicy1)
        self.le_search.setMaximumSize(QSize(150, 45))
        self.le_search.setFont(font2)

        self.horizontalLayout.addWidget(self.le_search)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.bt_save = QPushButton(Form)
        self.bt_save.setObjectName(u"bt_save")
        sizePolicy1.setHeightForWidth(self.bt_save.sizePolicy().hasHeightForWidth())
        self.bt_save.setSizePolicy(sizePolicy1)
        self.bt_save.setFont(font2)

        self.verticalLayout.addWidget(self.bt_save)

        self.bt_language = QPushButton(Form)
        self.bt_language.setObjectName(u"bt_language")
        sizePolicy1.setHeightForWidth(self.bt_language.sizePolicy().hasHeightForWidth())
        self.bt_language.setSizePolicy(sizePolicy1)
        self.bt_language.setFont(font2)

        self.verticalLayout.addWidget(self.bt_language)

        self.lb_word = QLabel(Form)
        self.lb_word.setObjectName(u"lb_word")
        self.lb_word.setMaximumSize(QSize(16777215, 16777215))
        self.lb_word.setFont(font2)

        self.verticalLayout.addWidget(self.lb_word)

        self.lw_result = QListWidget(Form)
        self.lw_result.setObjectName(u"lw_result")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lw_result.sizePolicy().hasHeightForWidth())
        self.lw_result.setSizePolicy(sizePolicy2)
        self.lw_result.setMaximumSize(QSize(16777215, 16777215))
        self.lw_result.setFont(font2)
        self.lw_result.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout.addWidget(self.lw_result)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"The Concordancer", None))
        self.lb_title.setText(QCoreApplication.translate("Form", u"The concordancer", None))
        self.lb_root_1.setText(QCoreApplication.translate("Form", u"The root :", None))
        self.lb_root.setText("")
        ___qtablewidgetitem = self.tb_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"The domain", None));
        ___qtablewidgetitem1 = self.tb_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"The concordances", None));
        self.bt_search.setText(QCoreApplication.translate("Form", u"Search", None))
        self.le_search.setPlaceholderText(QCoreApplication.translate("Form", u"Enter a word", None))
        self.bt_save.setText(QCoreApplication.translate("Form", u"Save the result", None))
        self.bt_language.setText(QCoreApplication.translate("Form", u"\u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.lb_word.setText(QCoreApplication.translate("Form", u"Derived words", None))
    # retranslateUi

