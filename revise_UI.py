# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revise_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(928, 850)
        MainWindow.setMinimumSize(QtCore.QSize(928, 850))
        MainWindow.setMaximumSize(QtCore.QSize(928, 850))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 10, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(630, 10, 71, 16))
        self.label_5.setObjectName("label_5")
        self.input_title = QtWidgets.QLineEdit(self.centralwidget)
        self.input_title.setGeometry(QtCore.QRect(30, 40, 113, 21))
        self.input_title.setObjectName("input_title")
        self.input_min = QtWidgets.QLineEdit(self.centralwidget)
        self.input_min.setGeometry(QtCore.QRect(180, 40, 113, 21))
        self.input_min.setObjectName("input_min")
        self.input_max = QtWidgets.QLineEdit(self.centralwidget)
        self.input_max.setGeometry(QtCore.QRect(320, 40, 113, 21))
        self.input_max.setObjectName("input_max")
        self.input_count = QtWidgets.QLineEdit(self.centralwidget)
        self.input_count.setGeometry(QtCore.QRect(470, 40, 113, 21))
        self.input_count.setObjectName("input_count")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(620, 40, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(480, 760, 55, 32))
        self.next_button.setObjectName("next_button")
        self.before_button = QtWidgets.QPushButton(self.centralwidget)
        self.before_button.setGeometry(QtCore.QRect(370, 760, 55, 32))
        self.before_button.setObjectName("before_button")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 150, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 741, 60, 16))
        self.label_10.setObjectName("label_10")
        self.change_title = QtWidgets.QLabel(self.centralwidget)
        self.change_title.setGeometry(QtCore.QRect(40, 110, 591, 16))
        self.change_title.setText("")
        self.change_title.setObjectName("change_title")
        self.change_kind = QtWidgets.QLabel(self.centralwidget)
        self.change_kind.setGeometry(QtCore.QRect(40, 170, 131, 16))
        self.change_kind.setText("")
        self.change_kind.setObjectName("change_kind")
        self.change_info_date = QtWidgets.QLabel(self.centralwidget)
        self.change_info_date.setGeometry(QtCore.QRect(210, 170, 131, 16))
        self.change_info_date.setText("")
        self.change_info_date.setObjectName("change_info_date")
        self.change_bid_number = QtWidgets.QLabel(self.centralwidget)
        self.change_bid_number.setGeometry(QtCore.QRect(370, 170, 131, 16))
        self.change_bid_number.setText("")
        self.change_bid_number.setObjectName("change_bid_number")
        self.change1 = QtWidgets.QLabel(self.centralwidget)
        self.change1.setGeometry(QtCore.QRect(40, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change1.setFont(font)
        self.change1.setText("")
        self.change1.setObjectName("change1")
        self.change3 = QtWidgets.QLabel(self.centralwidget)
        self.change3.setGeometry(QtCore.QRect(40, 290, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change3.setFont(font)
        self.change3.setText("")
        self.change3.setObjectName("change3")
        self.change5 = QtWidgets.QLabel(self.centralwidget)
        self.change5.setGeometry(QtCore.QRect(40, 330, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change5.setFont(font)
        self.change5.setText("")
        self.change5.setObjectName("change5")
        self.change2 = QtWidgets.QLabel(self.centralwidget)
        self.change2.setGeometry(QtCore.QRect(380, 250, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change2.setFont(font)
        self.change2.setText("")
        self.change2.setObjectName("change2")
        self.change4 = QtWidgets.QLabel(self.centralwidget)
        self.change4.setGeometry(QtCore.QRect(380, 290, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change4.setFont(font)
        self.change4.setText("")
        self.change4.setObjectName("change4")
        self.change6 = QtWidgets.QLabel(self.centralwidget)
        self.change6.setGeometry(QtCore.QRect(380, 330, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change6.setFont(font)
        self.change6.setText("")
        self.change6.setObjectName("change6")
        self.change_1_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_1_answer.setGeometry(QtCore.QRect(190, 250, 171, 16))
        self.change_1_answer.setText("")
        self.change_1_answer.setObjectName("change_1_answer")
        self.change_3_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_3_answer.setGeometry(QtCore.QRect(190, 290, 171, 16))
        self.change_3_answer.setText("")
        self.change_3_answer.setObjectName("change_3_answer")
        self.change_5_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_5_answer.setGeometry(QtCore.QRect(190, 330, 171, 16))
        self.change_5_answer.setText("")
        self.change_5_answer.setObjectName("change_5_answer")
        self.change_2_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_2_answer.setGeometry(QtCore.QRect(530, 250, 171, 16))
        self.change_2_answer.setText("")
        self.change_2_answer.setObjectName("change_2_answer")
        self.change_4_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_4_answer.setGeometry(QtCore.QRect(530, 290, 171, 16))
        self.change_4_answer.setText("")
        self.change_4_answer.setObjectName("change_4_answer")
        self.change_6_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_6_answer.setGeometry(QtCore.QRect(530, 330, 171, 16))
        self.change_6_answer.setText("")
        self.change_6_answer.setObjectName("change_6_answer")
        self.change7 = QtWidgets.QLabel(self.centralwidget)
        self.change7.setGeometry(QtCore.QRect(40, 370, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change7.setFont(font)
        self.change7.setText("")
        self.change7.setObjectName("change7")
        self.change8 = QtWidgets.QLabel(self.centralwidget)
        self.change8.setGeometry(QtCore.QRect(380, 370, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change8.setFont(font)
        self.change8.setText("")
        self.change8.setObjectName("change8")
        self.change_7_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_7_answer.setGeometry(QtCore.QRect(190, 370, 171, 16))
        self.change_7_answer.setText("")
        self.change_7_answer.setObjectName("change_7_answer")
        self.change_8_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_8_answer.setGeometry(QtCore.QRect(530, 370, 171, 20))
        self.change_8_answer.setText("")
        self.change_8_answer.setObjectName("change_8_answer")
        self.change_4_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_4_answer_2.setGeometry(QtCore.QRect(530, 540, 161, 16))
        self.change_4_answer_2.setText("")
        self.change_4_answer_2.setObjectName("change_4_answer_2")
        self.change7_2 = QtWidgets.QLabel(self.centralwidget)
        self.change7_2.setGeometry(QtCore.QRect(40, 620, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change7_2.setFont(font)
        self.change7_2.setText("")
        self.change7_2.setObjectName("change7_2")
        self.change2_2 = QtWidgets.QLabel(self.centralwidget)
        self.change2_2.setGeometry(QtCore.QRect(380, 500, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change2_2.setFont(font)
        self.change2_2.setText("")
        self.change2_2.setObjectName("change2_2")
        self.change_3_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_3_answer_2.setGeometry(QtCore.QRect(190, 540, 171, 16))
        self.change_3_answer_2.setText("")
        self.change_3_answer_2.setObjectName("change_3_answer_2")
        self.change3_2 = QtWidgets.QLabel(self.centralwidget)
        self.change3_2.setGeometry(QtCore.QRect(40, 540, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change3_2.setFont(font)
        self.change3_2.setText("")
        self.change3_2.setObjectName("change3_2")
        self.change8_2 = QtWidgets.QLabel(self.centralwidget)
        self.change8_2.setGeometry(QtCore.QRect(380, 620, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change8_2.setFont(font)
        self.change8_2.setText("")
        self.change8_2.setObjectName("change8_2")
        self.change_1_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_1_answer_2.setGeometry(QtCore.QRect(190, 500, 171, 16))
        self.change_1_answer_2.setText("")
        self.change_1_answer_2.setObjectName("change_1_answer_2")
        self.change_5_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_5_answer_2.setGeometry(QtCore.QRect(190, 580, 171, 16))
        self.change_5_answer_2.setText("")
        self.change_5_answer_2.setObjectName("change_5_answer_2")
        self.change_2_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_2_answer_2.setGeometry(QtCore.QRect(530, 500, 161, 16))
        self.change_2_answer_2.setText("")
        self.change_2_answer_2.setObjectName("change_2_answer_2")
        self.change_8_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_8_answer_2.setGeometry(QtCore.QRect(530, 620, 161, 16))
        self.change_8_answer_2.setText("")
        self.change_8_answer_2.setObjectName("change_8_answer_2")
        self.change4_2 = QtWidgets.QLabel(self.centralwidget)
        self.change4_2.setGeometry(QtCore.QRect(380, 540, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change4_2.setFont(font)
        self.change4_2.setText("")
        self.change4_2.setObjectName("change4_2")
        self.change6_2 = QtWidgets.QLabel(self.centralwidget)
        self.change6_2.setGeometry(QtCore.QRect(380, 580, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change6_2.setFont(font)
        self.change6_2.setText("")
        self.change6_2.setObjectName("change6_2")
        self.change_7_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_7_answer_2.setGeometry(QtCore.QRect(190, 620, 171, 16))
        self.change_7_answer_2.setText("")
        self.change_7_answer_2.setObjectName("change_7_answer_2")
        self.change_6_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_6_answer_2.setGeometry(QtCore.QRect(530, 580, 171, 16))
        self.change_6_answer_2.setText("")
        self.change_6_answer_2.setObjectName("change_6_answer_2")
        self.change1_2 = QtWidgets.QLabel(self.centralwidget)
        self.change1_2.setGeometry(QtCore.QRect(40, 500, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change1_2.setFont(font)
        self.change1_2.setText("")
        self.change1_2.setObjectName("change1_2")
        self.change5_2 = QtWidgets.QLabel(self.centralwidget)
        self.change5_2.setGeometry(QtCore.QRect(40, 580, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change5_2.setFont(font)
        self.change5_2.setText("")
        self.change5_2.setObjectName("change5_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(710, 100, 191, 600))
        self.listWidget.setObjectName("listWidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 210, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 450, 711, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(780, 30, 50, 32))
        self.search_button.setObjectName("search_button")
        self.change10 = QtWidgets.QLabel(self.centralwidget)
        self.change10.setGeometry(QtCore.QRect(380, 410, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change10.setFont(font)
        self.change10.setText("")
        self.change10.setObjectName("change10")
        self.change_9_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_9_answer.setGeometry(QtCore.QRect(190, 410, 171, 16))
        self.change_9_answer.setText("")
        self.change_9_answer.setObjectName("change_9_answer")
        self.change9 = QtWidgets.QLabel(self.centralwidget)
        self.change9.setGeometry(QtCore.QRect(40, 410, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change9.setFont(font)
        self.change9.setText("")
        self.change9.setObjectName("change9")
        self.change_10_answer = QtWidgets.QLabel(self.centralwidget)
        self.change_10_answer.setGeometry(QtCore.QRect(530, 410, 171, 20))
        self.change_10_answer.setText("")
        self.change_10_answer.setObjectName("change_10_answer")
        self.change_10_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_10_answer_2.setGeometry(QtCore.QRect(530, 660, 161, 16))
        self.change_10_answer_2.setText("")
        self.change_10_answer_2.setObjectName("change_10_answer_2")
        self.change_9_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_9_answer_2.setGeometry(QtCore.QRect(190, 660, 171, 16))
        self.change_9_answer_2.setText("")
        self.change_9_answer_2.setObjectName("change_9_answer_2")
        self.change9_2 = QtWidgets.QLabel(self.centralwidget)
        self.change9_2.setGeometry(QtCore.QRect(40, 660, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change9_2.setFont(font)
        self.change9_2.setText("")
        self.change9_2.setObjectName("change9_2")
        self.change10_2 = QtWidgets.QLabel(self.centralwidget)
        self.change10_2.setGeometry(QtCore.QRect(380, 660, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change10_2.setFont(font)
        self.change10_2.setText("")
        self.change10_2.setObjectName("change10_2")
        self.change_12_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_12_answer_2.setGeometry(QtCore.QRect(530, 700, 161, 16))
        self.change_12_answer_2.setText("")
        self.change_12_answer_2.setObjectName("change_12_answer_2")
        self.change_11_answer_2 = QtWidgets.QLabel(self.centralwidget)
        self.change_11_answer_2.setGeometry(QtCore.QRect(190, 700, 171, 16))
        self.change_11_answer_2.setText("")
        self.change_11_answer_2.setObjectName("change_11_answer_2")
        self.change11_2 = QtWidgets.QLabel(self.centralwidget)
        self.change11_2.setGeometry(QtCore.QRect(40, 700, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change11_2.setFont(font)
        self.change11_2.setText("")
        self.change11_2.setObjectName("change11_2")
        self.change12_2 = QtWidgets.QLabel(self.centralwidget)
        self.change12_2.setGeometry(QtCore.QRect(380, 700, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.change12_2.setFont(font)
        self.change12_2.setText("")
        self.change12_2.setObjectName("change12_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(640, 730, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.change_link = QtWidgets.QLineEdit(self.centralwidget)
        self.change_link.setGeometry(QtCore.QRect(82, 739, 551, 21))
        self.change_link.setDragEnabled(True)
        self.change_link.setReadOnly(True)
        self.change_link.setObjectName("change_link")
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setGeometry(QtCore.QRect(20, 800, 350, 16))
        self.notice.setText("크롤링 개수는 100이하만 가능합니다")
        self.state = QtWidgets.QLabel(self.centralwidget)
        self.state.setGeometry(QtCore.QRect(440,800,400,20))
        self.state.setText("대기중 - 검색시 완료가 뜰때까지 기다려주세요")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 928, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.next_button.clicked.connect(MainWindow.click_next)
        self.before_button.clicked.connect(MainWindow.click_before)
        self.search_button.clicked.connect(MainWindow.click_search)
        self.pushButton.clicked.connect(MainWindow.click_link)
        self.listWidget.itemClicked['QListWidgetItem*'].connect(MainWindow.click_title)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "공고명"))
        self.label_2.setText(_translate("MainWindow", "최소추정가격"))
        self.label_3.setText(_translate("MainWindow", "최대추정가격"))
        self.label_4.setText(_translate("MainWindow", "크롤링개수"))
        self.label_5.setText(_translate("MainWindow", "지역"))
        self.comboBox.setItemText(0, _translate("MainWindow", "전국"))
        self.comboBox.setItemText(1, _translate("MainWindow", "서울"))
        self.comboBox.setItemText(2, _translate("MainWindow", "부산"))
        self.comboBox.setItemText(3, _translate("MainWindow", "인천"))
        self.comboBox.setItemText(4, _translate("MainWindow", "대구"))
        self.comboBox.setItemText(5, _translate("MainWindow", "광주"))
        self.comboBox.setItemText(6, _translate("MainWindow", "대전"))
        self.comboBox.setItemText(7, _translate("MainWindow", "울산"))
        self.comboBox.setItemText(8, _translate("MainWindow", "세종"))
        self.comboBox.setItemText(9, _translate("MainWindow", "경기"))
        self.comboBox.setItemText(10, _translate("MainWindow", "강원"))
        self.comboBox.setItemText(11, _translate("MainWindow", "충북"))
        self.comboBox.setItemText(12, _translate("MainWindow", "충남"))
        self.comboBox.setItemText(13, _translate("MainWindow", "전북"))
        self.comboBox.setItemText(14, _translate("MainWindow", "전남"))
        self.comboBox.setItemText(15, _translate("MainWindow", "경북"))
        self.comboBox.setItemText(16, _translate("MainWindow", "경남"))
        self.comboBox.setItemText(17, _translate("MainWindow", "제주"))
        self.next_button.setText(_translate("MainWindow", "다음"))
        self.before_button.setText(_translate("MainWindow", "이전"))
        self.label_6.setText(_translate("MainWindow", "공고명"))
        self.label_7.setText(_translate("MainWindow", "공고종류"))
        self.label_8.setText(_translate("MainWindow", "게시일시"))
        self.label_9.setText(_translate("MainWindow", "입찰공고번호"))
        self.label_10.setText(_translate("MainWindow", "링크 - "))
        self.search_button.setText(_translate("MainWindow", "검색"))
        self.pushButton.setText(_translate("MainWindow", "링크로이동"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

