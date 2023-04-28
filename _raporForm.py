# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_raporForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainRaporKontrol(object):
    def setupUi(self, MainRaporKontrol):
        MainRaporKontrol.setObjectName("MainRaporKontrol")
        MainRaporKontrol.resize(2323, 1005)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainRaporKontrol.sizePolicy().hasHeightForWidth())
        MainRaporKontrol.setSizePolicy(sizePolicy)
        MainRaporKontrol.setMinimumSize(QtCore.QSize(1900, 700))
        MainRaporKontrol.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainRaporKontrol.setFont(font)
        MainRaporKontrol.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resim/kaynakjpg/Hitchhiker-Symbol-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainRaporKontrol.setWindowIcon(icon)
        MainRaporKontrol.setStyleSheet("#centralwidget{\n"
"    background-image: url(:/rcc/kaynak/hemesback.jpg);\n"
"\n"
"}\n"
"")
        MainRaporKontrol.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainRaporKontrol)
        self.centralwidget.setStyleSheet("#centralwidget{border-image: url(:/resim/kaynakjpg/dpanic3.jpg);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 520, 1871, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableProducts = QtWidgets.QTableWidget(self.tab)
        self.tableProducts.setGeometry(QtCore.QRect(20, 10, 1841, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableProducts.setFont(font)
        self.tableProducts.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.tableProducts.setObjectName("tableProducts")
        self.tableProducts.setColumnCount(0)
        self.tableProducts.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableProducts_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableProducts_2.setGeometry(QtCore.QRect(20, 10, 1841, 371))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tableProducts_2.setFont(font)
        self.tableProducts_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.tableProducts_2.setObjectName("tableProducts_2")
        self.tableProducts_2.setColumnCount(0)
        self.tableProducts_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        self.btnSelectFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFile.setGeometry(QtCore.QRect(200, 70, 361, 69))
        self.btnSelectFile.setStyleSheet("font: 75 12pt  \"Snap ITC\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 44, 97);")
        self.btnSelectFile.setIconSize(QtCore.QSize(60, 60))
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setGeometry(QtCore.QRect(200, 200, 361, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btnStart.setFont(font)
        self.btnStart.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.btnStart.setAcceptDrops(False)
        self.btnStart.setStyleSheet("font: 75 13pt  \"Snap ITC\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(28, 44, 97);")
        self.btnStart.setIconSize(QtCore.QSize(70, 70))
        self.btnStart.setObjectName("btnStart")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 150, 351, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.txtDosyaYolLoad = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtDosyaYolLoad.setEnabled(False)
        self.txtDosyaYolLoad.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.txtDosyaYolLoad.setDragEnabled(True)
        self.txtDosyaYolLoad.setClearButtonEnabled(True)
        self.txtDosyaYolLoad.setObjectName("txtDosyaYolLoad")
        self.gridLayout_4.addWidget(self.txtDosyaYolLoad, 0, 1, 1, 1)
        MainRaporKontrol.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainRaporKontrol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2323, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuSecenekler = QtWidgets.QMenu(self.menubar)
        self.menuSecenekler.setObjectName("menuSecenekler")
        MainRaporKontrol.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainRaporKontrol)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainRaporKontrol.setStatusBar(self.statusbar)
        self.actionExcel = QtWidgets.QAction(MainRaporKontrol)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resim/kaynakjpg/Microsoft-Office-Excel-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExcel.setIcon(icon1)
        self.actionExcel.setObjectName("actionExcel")
        self.actionDosya_Yukle = QtWidgets.QAction(MainRaporKontrol)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/rcc/hermes_sh.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDosya_Yukle.setIcon(icon2)
        self.actionDosya_Yukle.setObjectName("actionDosya_Yukle")
        self.actionSil = QtWidgets.QAction(MainRaporKontrol)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resim/kaynakjpg/table-remove-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSil.setIcon(icon3)
        self.actionSil.setObjectName("actionSil")
        self.menuSecenekler.addSeparator()
        self.menuSecenekler.addSeparator()
        self.menuSecenekler.addAction(self.actionExcel)
        self.menuSecenekler.addSeparator()
        self.menuSecenekler.addSeparator()
        self.menuSecenekler.addAction(self.actionSil)
        self.menubar.addAction(self.menuSecenekler.menuAction())

        self.retranslateUi(MainRaporKontrol)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainRaporKontrol)

    def retranslateUi(self, MainRaporKontrol):
        _translate = QtCore.QCoreApplication.translate
        MainRaporKontrol.setWindowTitle(_translate("MainRaporKontrol", "Rapor Kontrol"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainRaporKontrol", "Rapor Listesi"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainRaporKontrol", "YOK"))
        self.btnSelectFile.setText(_translate("MainRaporKontrol", "DOSYA\n"
" SEÇ"))
        self.btnStart.setToolTip(_translate("MainRaporKontrol", "CTRL+D"))
        self.btnStart.setText(_translate("MainRaporKontrol", "BAŞLAT...!"))
        self.btnStart.setShortcut(_translate("MainRaporKontrol", "Ctrl+D"))
        self.label_11.setText(_translate("MainRaporKontrol", "Seçilen Dosya: "))
        self.menuSecenekler.setTitle(_translate("MainRaporKontrol", "Seçenekler"))
        self.actionExcel.setText(_translate("MainRaporKontrol", "Excele Aktar"))
        self.actionExcel.setToolTip(_translate("MainRaporKontrol", "Excele Aktar"))
        self.actionDosya_Yukle.setText(_translate("MainRaporKontrol", "Dosya Yükle"))
        self.actionDosya_Yukle.setToolTip(_translate("MainRaporKontrol", "Dosya Yükle"))
        self.actionSil.setText(_translate("MainRaporKontrol", "Tabloyu Sil"))
        self.actionSil.setToolTip(_translate("MainRaporKontrol", "Tabloyu Sil"))
import kaynak_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainRaporKontrol = QtWidgets.QMainWindow()
    ui = Ui_MainRaporKontrol()
    ui.setupUi(MainRaporKontrol)
    MainRaporKontrol.show()
    sys.exit(app.exec_())
