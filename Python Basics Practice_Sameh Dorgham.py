
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.setWindowTitle("PyVideoPlayer")

window.setWindowIcon(QtGui.QIcon("Python.png"))

window.setGeometry(400,300,800,500)



def browse():
    browser = QtWidgets.QFileDialog.getOpenFileName(window)


btn_Browse = QtWidgets.QPushButton("Browse", window)

btn_Browse.setGeometry(200,200,150,80)

#btn_Browse.setStyleSheet('background-color:blue; color:white; font-size:18px;')

btn_Browse.setIcon(QtGui.QIcon("Python.png"))

btn_Browse.clicked.connect(browse)



btn_Close = QtWidgets.QPushButton("Close", window)

btn_Close.setGeometry(200,300,150,80)

btn_Close.setToolTip("Click to Exit")

btn_Close.setIcon(QtGui.QIcon("Python.png"))

btn_Close.clicked.connect(exit)


text = QtWidgets.QLineEdit(window)

text.setGeometry(200,40,150,30)


radio1 = QtWidgets.QRadioButton("HTML", window)

radio1.setGeometry(200,120,150,30)

radio2 = QtWidgets.QRadioButton("CSS", window)

radio2.setGeometry(200,140,150,30)

radio3 = QtWidgets.QRadioButton("Python", window)

radio3.setGeometry(200,160,150,30)



chek1 = QtWidgets.QCheckBox("HTML", window)

chek1.setGeometry(300,120,150,30)

chek2 = QtWidgets.QCheckBox("CSS", window)

chek2.setGeometry(300,140,150,30)

chek3 = QtWidgets.QCheckBox("Python", window)

chek3.setGeometry(300,160,150,30)


cbo1 = QtWidgets.QComboBox(window)

cbo1.setGeometry(300,40,150,30)

cbo1.addItem("")
cbo1.addItem("Egypt")
cbo1.addItem("Saudia")
cbo1.addItem("Kwait")
cbo1.addItem("Jordan")
cbo1.addItem("Bahrain")


"""
label = QtWidgets.QLabel(window)
pixmap = QPixmap("Python.png").scaled(600,400)
label.setPixmap(pixmap)
"""


"""
message1 = QtWidgets.QMessageBox.question(window, "Python ..." , "are you sure ?")
message2 = QtWidgets.QMessageBox.warning(window,"Exit", "are you sure ?")
message3 = QtWidgets.QMessageBox.information(window, "info", "info ....")
message4 = QtWidgets.QMessageBox.about(window, "info", "info ....")
errmessage = QtWidgets.QErrorMessage(window)
errmessage.showMessage("Please install PyQt5 to run the program")
"""


def message():

    m = QtWidgets.QMessageBox.question(window,"warining" , "you are closing the program!")
    
    if m == QtWidgets.QMessageBox.Yes:
        print("the program will close now")
    else:
        print("you canceld the command")


btn = QtWidgets.QPushButton("Close App", window)

btn.clicked.connect(message)



tab = QtWidgets.QTabWidget(window)

#tab.resize(600,400)

t1 = QtWidgets.QWidget()
t2 = QtWidgets.QWidget()
t3 = QtWidgets.QWidget()
t4 = QtWidgets.QWidget()

tab.addTab(t1,"tab one")
tab.addTab(t2,"tab tow")
tab.addTab(t3,"tab three")
tab.addTab(t4,"tab four")


def fonts():
    font = QtWidgets.QFontDialog.getFont()


btn_font = QtWidgets.QPushButton("Choose Font:", window)

btn_font.move(50,100)

btn_font.clicked.connect(fonts)


def colors():
    color = QtWidgets.QColorDialog.getColor()

btn_color = QtWidgets.QPushButton("choose color:", window)

btn_color.move(50,140)

btn_color.clicked.connect(colors)


calendar = QtWidgets.QCalendarWidget(window)

calendar.move(400,200)


window.show()

app.exec_()

