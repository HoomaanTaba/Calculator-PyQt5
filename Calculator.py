# Calculator
# Created by :   @HoomaanTaba

from PyQt5 import QtCore, QtGui, QtWidgets
from math import sqrt
import sys

class Ui_MainWindow():
    def setupUi(self, MainWindow): 
        #Fonts
        default_font = QtGui.QFont()  # MS Shell Dlg 2 font
        default_font.setPointSize(25)   # Default font size
        Arial_font = QtGui.QFont("Arial") # Arial font
        Arial_font.setPointSize(25)   # Default font size
        Sakkal_Majalla_font = QtGui.QFont("Sakkal Majalla") # Sakkal Majalla font
        Sakkal_Majalla_font.setPointSize(18) # Default size

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Calculator_Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowTitle("Calculator")
        MainWindow.resize(276, 490)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setFixedSize(MainWindow.size())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 276, 51))
        Arial_font.setPointSize(26)
        self.lineEdit.setFont(Arial_font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
        "background-color: rgb(170, 255, 255);")
        self.lineEdit.setFrame(False)
        self.lineEdit.setMaxLength(14)

        # Phrase lineEdit: Top lineEdit which shows completed mathematical phrase
        self.phrase_LineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phrase_LineEdit.setEnabled(False)
        self.phrase_LineEdit.setGeometry(QtCore.QRect(0, 0, 276, 31))
        default_font.setPointSize(15)
        self.phrase_LineEdit.setFont(default_font)
        self.phrase_LineEdit.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.phrase_LineEdit.setFrame(False)
        self.phrase_LineEdit.setMaxLength(14)

        # Numbers' buttons
        self.b_0 = QtWidgets.QPushButton(self.centralwidget)
        self.b_0.setText("0")
        self.b_0.setGeometry(QtCore.QRect(68, 420, 71, 71))
        Arial_font.setPointSize(25)
        self.b_0.setFont(Arial_font)
        self.b_0.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_0.setShortcut("0")
        self.b_0.clicked.connect(lambda:self.button_pressed("0"))

        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setText("1")
        self.b_1.setGeometry(QtCore.QRect(-1, 351, 71, 71))
        Arial_font.setPointSize(25)
        self.b_1.setFont(Arial_font)
        self.b_1.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_1.setShortcut("1")
        self.b_1.clicked.connect(lambda:self.button_pressed("1"))

        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setText("2")
        self.b_2.setGeometry(QtCore.QRect(68, 351, 71, 71))
        Arial_font.setPointSize(25)
        self.b_2.setFont(Arial_font)
        self.b_2.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_2.setShortcut("2")
        self.b_2.clicked.connect(lambda:self.button_pressed("2"))

        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setText("3")
        self.b_3.setGeometry(QtCore.QRect(137, 351, 71, 71))
        Arial_font.setPointSize(25)
        self.b_3.setFont(Arial_font)
        self.b_3.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_3.setShortcut("3")
        self.b_3.clicked.connect(lambda:self.button_pressed("3"))

        self.b_4 = QtWidgets.QPushButton(self.centralwidget)
        self.b_4.setText("4")
        self.b_4.setGeometry(QtCore.QRect(-1, 282, 71, 71))
        Arial_font.setPointSize(25)
        self.b_4.setFont(Arial_font)
        self.b_4.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_4.setShortcut("4")
        self.b_4.clicked.connect(lambda:self.button_pressed("4"))

        self.b_5 = QtWidgets.QPushButton(self.centralwidget)
        self.b_5.setText("5")
        self.b_5.setGeometry(QtCore.QRect(68, 282, 71, 71))
        Arial_font.setPointSize(25)
        self.b_5.setFont(Arial_font)
        self.b_5.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_5.setShortcut("5")
        self.b_5.clicked.connect(lambda:self.button_pressed("5"))

        self.b_6 = QtWidgets.QPushButton(self.centralwidget)
        self.b_6.setText("6")
        self.b_6.setGeometry(QtCore.QRect(137, 282, 71, 71))
        Arial_font.setPointSize(25)
        self.b_6.setFont(Arial_font)
        self.b_6.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")  
        self.b_6.setShortcut("6") 
        self.b_6.clicked.connect(lambda:self.button_pressed("6"))

        self.b_7 = QtWidgets.QPushButton(self.centralwidget)
        self.b_7.setText("7")
        self.b_7.setGeometry(QtCore.QRect(-1, 213, 71, 71))
        Arial_font.setPointSize(25)
        self.b_7.setFont(Arial_font)
        self.b_7.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_7.setShortcut("7")
        self.b_7.clicked.connect(lambda:self.button_pressed("7"))

        self.b_8 = QtWidgets.QPushButton(self.centralwidget)
        self.b_8.setText("8")
        self.b_8.setGeometry(QtCore.QRect(68, 213, 71, 71))
        Arial_font.setPointSize(25)
        self.b_8.setFont(Arial_font)
        self.b_8.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_8.setShortcut("8")
        self.b_8.clicked.connect(lambda:self.button_pressed("8"))

        self.b_9 = QtWidgets.QPushButton(self.centralwidget)
        self.b_9.setText("9")
        self.b_9.setGeometry(QtCore.QRect(137, 213, 71, 71))
        Arial_font.setPointSize(25)
        self.b_9.setFont(Arial_font)
        self.b_9.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_9.setShortcut("9")
        self.b_9.clicked.connect(lambda:self.button_pressed("9"))

        self.b_multiplication = QtWidgets.QPushButton(self.centralwidget)
        self.b_multiplication.setText("×")
        self.b_multiplication.setGeometry(QtCore.QRect(206, 144, 71, 71))
        Arial_font.setPointSize(25)
        self.b_multiplication.setFont(Arial_font)
        self.b_multiplication.setStyleSheet("background-color: rgb(139, 0, 209);\n"
        "color: rgb(255, 255, 255);")
        self.b_multiplication.setShortcut("*")
        self.b_multiplication.clicked.connect(lambda:self.button_pressed("×"))

        self.b_division = QtWidgets.QPushButton(self.centralwidget)
        self.b_division.setText("÷")
        self.b_division.setGeometry(QtCore.QRect(206, 213, 71, 71))
        Arial_font.setPointSize(25)
        self.b_division.setFont(Arial_font)
        self.b_division.setStyleSheet("background-color: rgb(139, 0, 209);\n"
        "color: rgb(255, 255, 255);")
        self.b_division.setShortcut("/")
        self.b_division.clicked.connect(lambda:self.button_pressed("÷"))

        self.b_addition = QtWidgets.QPushButton(self.centralwidget)
        self.b_addition.setText("+")
        self.b_addition.setGeometry(QtCore.QRect(206, 282, 71, 71))
        Arial_font.setPointSize(25)
        self.b_addition.setFont(Arial_font)
        self.b_addition.setStyleSheet("background-color: rgb(139, 0, 209);\n"
        "color: rgb(255, 255, 255);")
        self.b_addition.setShortcut("+")
        self.b_addition.clicked.connect(lambda:self.button_pressed("+"))

        self.b_subtraction = QtWidgets.QPushButton(self.centralwidget)
        self.b_subtraction.setText("-")
        self.b_subtraction.setGeometry(QtCore.QRect(206, 351, 71, 71))
        Arial_font.setPointSize(25)
        self.b_subtraction.setFont(Arial_font)
        self.b_subtraction.setStyleSheet("background-color: rgb(139, 0, 209);\n"
        "color: rgb(255, 255, 255);")
        self.b_subtraction.setShortcut("-")
        self.b_subtraction.clicked.connect(lambda:self.button_pressed("-"))

        self.b_thePowerOf = QtWidgets.QPushButton(self.centralwidget)
        self.b_thePowerOf.setText("xʸ")
        self.b_thePowerOf.setGeometry(QtCore.QRect(137, 144, 71, 71))
        Arial_font.setPointSize(25)
        self.b_thePowerOf.setFont(Arial_font)
        self.b_thePowerOf.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_thePowerOf.setShortcut("^")
        self.b_thePowerOf.clicked.connect(lambda:self.button_pressed("^"))

        self.b_radical = QtWidgets.QPushButton(self.centralwidget)
        self.b_radical.setText("√")
        self.b_radical.setGeometry(QtCore.QRect(68, 144, 71, 71))
        default_font.setPointSize(25)
        self.b_radical.setFont(default_font)
        self.b_radical.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_radical.setShortcut("Alt+X")
        self.b_radical.clicked.connect(lambda:self.radical_pressed())

        self.b_posORneg = QtWidgets.QPushButton(self.centralwidget)
        self.b_posORneg.setText("±")
        self.b_posORneg.setGeometry(QtCore.QRect(206, 75, 71, 71))
        Arial_font.setPointSize(25)
        self.b_posORneg.setFont(Arial_font)
        self.b_posORneg.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_posORneg.setShortcut("Alt+N")
        self.b_posORneg.clicked.connect(lambda:self.posORneg_pressed())

        self.b_percentage = QtWidgets.QPushButton(self.centralwidget)
        self.b_percentage.setText("%")
        self.b_percentage.setGeometry(QtCore.QRect(137, 75, 71, 71))
        Arial_font.setPointSize(25)
        self.b_percentage.setFont(Arial_font)
        self.b_percentage.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_percentage.setShortcut("%")
        self.b_percentage.clicked.connect(lambda:self.percentage_pressed())
        
        self.b_divisionByX = QtWidgets.QPushButton(self.centralwidget)
        self.b_divisionByX.setText("⅟\u2006x")
        self.b_divisionByX.setGeometry(QtCore.QRect(-1, 144, 71, 71))
        Arial_font.setPointSize(21)
        self.b_divisionByX.setFont(Arial_font)
        self.b_divisionByX.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_divisionByX.setShortcut("Ctrl+X")
        self.b_divisionByX.clicked.connect(lambda:self.devisionByx_pressed())

        self.b_point = QtWidgets.QPushButton(self.centralwidget)
        self.b_point.setText(".")
        self.b_point.setGeometry(QtCore.QRect(-1, 420, 71, 71))
        Arial_font.setBold(True)
        Arial_font.setPointSize(25)
        self.b_point.setFont(Arial_font)
        self.b_point.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_point.setShortcut(".")
        Arial_font.setBold(False)
        self.b_point.clicked.connect(lambda:self.button_pressed("."))
        
        self.b_equal = QtWidgets.QPushButton(self.centralwidget)
        self.b_equal.setText("=")
        self.b_equal.setGeometry(QtCore.QRect(206, 420, 71, 71))
        Arial_font.setPointSize(25)
        self.b_equal.setFont(Arial_font)
        self.b_equal.setStyleSheet("background-color: rgb(255, 194, 10);\n"
        "color: rgb(255, 255, 255);")
        self.b_equal.setShortcut("Return")
        self.b_equal.clicked.connect(lambda:self.claculate())
        
        self.b_backspace = QtWidgets.QPushButton(self.centralwidget)
        self.b_backspace.setText("⌫")
        self.b_backspace.setGeometry(QtCore.QRect(137, 420, 71, 71))
        Arial_font.setPointSize(23)
        self.b_backspace.setFont(Arial_font)
        self.b_backspace.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_backspace.setShortcut("Backspace")
        self.b_backspace.clicked.connect(lambda:self.backspace_pressed())
        
        self.b_clearEntry = QtWidgets.QPushButton(self.centralwidget)
        self.b_clearEntry.setText("CE")
        self.b_clearEntry.setGeometry(QtCore.QRect(-1, 75, 71, 71))
        default_font.setPointSize(22)
        self.b_clearEntry.setFont(default_font)
        self.b_clearEntry.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_clearEntry.setShortcut("Delete")
        self.b_clearEntry.clicked.connect(lambda:self.clearEntry_pressed())

        self.b_clear = QtWidgets.QPushButton(self.centralwidget)
        self.b_clear.setText("C")
        self.b_clear.setGeometry(QtCore.QRect(68, 75, 71, 71))
        default_font.setPointSize(22)
        self.b_clear.setFont(default_font)
        self.b_clear.setStyleSheet("background-color: rgb(85, 85, 85);\n"
        "color: rgb(255, 255, 255);")
        self.b_clear.setShortcut("Esc")
        self.b_clear.clicked.connect(lambda:self.clear_pressed())
        
        # Top help question mark
        self.help_label = QtWidgets.QLabel(self.centralwidget)
        self.help_label.setText("?")
        self.help_label.setGeometry(260,0,21,31)
        Sakkal_Majalla_font.setBold(True)
        self.help_label.setFont(Sakkal_Majalla_font)
        self.help_label.setStyleSheet("color: rgb(94, 94, 94);")
        self.help_label.setToolTip("***@HoomaanTaba***\n\n""Shortcuts:\n"
        "0,1,...,9 : Numbers on keyboard\n""C : Esc\n""CE : Delete\n"
        "% : Shift + 5\n""± : Alt + N\n""1/x : Ctrl + X\n""√ : Alt + X\n"
        "xʸ : Shift + 6\n""× : Shift + 8\n""÷ : /\n""+ : Shift + =\n"
        "- : -\n"". : .\n""= : Enter\n""⌫ : Backspace")
        
        # Set Buttons' layers
        self.phrase_LineEdit.raise_()
        self.lineEdit.raise_()
        self.b_clearEntry.raise_()
        self.b_clear.raise_() 
        self.b_percentage.raise_()
        self.b_posORneg.raise_()
        self.b_divisionByX.raise_()
        self.b_radical.raise_()  
        self.b_thePowerOf.raise_()
        self.b_multiplication.raise_()
        self.b_7.raise_()
        self.b_8.raise_()
        self.b_9.raise_()
        self.b_division.raise_()
        self.b_4.raise_()
        self.b_5.raise_()
        self.b_6.raise_()
        self.b_addition.raise_()
        self.b_1.raise_()
        self.b_2.raise_()
        self.b_3.raise_()
        self.b_subtraction.raise_()
        self.b_point.raise_()
        self.b_0.raise_()
        self.b_backspace.raise_()
        self.b_equal.raise_()
        self.help_label.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
            
    # The function that connect buttons & lineEdits    
    def button_pressed(self,text):
        linetext = self.lineEdit.text()
        self.phrase_LineEdit.setText(self.phrase_LineEdit.text()+text)
        if text=="×" or text=="÷" or text=="+" or text=="-" or text=="^":
            self.lineEdit.setText(text)
        else:
            if linetext=="×" or linetext=="÷" or linetext=="+" or linetext=="-" or linetext=="^" or linetext=="Error":
                self.lineEdit.setText(text)
            else:
                self.lineEdit.setText(self.lineEdit.text()+text)

    def radical_pressed(self):
        try:
            self.lineEdit.setText(str(sqrt(eval(self.phrase_LineEdit.text()))))
            self.phrase_LineEdit.setText(str(sqrt(eval(self.phrase_LineEdit.text()))))
        except:
            if self.lineEdit.text() == "":
                pass
            else:
                self.phrase_LineEdit.setText("")
                self.lineEdit.setText("Error")

    # Positive or negative numbers
    def posORneg_pressed(self):
        remove_char = lambda string,n:string[:n] + string[n+1:]
        add_char = lambda string,n,char:string[:n]+char+string[n:]
        try:
            if float(self.lineEdit.text())<0:
                self.phrase_LineEdit.setText(remove_char(self.phrase_LineEdit.text(),-len(self.lineEdit.text())))
                self.lineEdit.setText(self.lineEdit.text()[1:])
            elif float(self.lineEdit.text())>0:
                self.phrase_LineEdit.setText(add_char(self.phrase_LineEdit.text(),-len(self.lineEdit.text()),"-"))
                self.lineEdit.setText("-"+self.lineEdit.text())
        except:
            pass

    def percentage_pressed(self):
        try:
            self.phrase_LineEdit.setText(self.phrase_LineEdit.text()[:-len(self.lineEdit.text())])
            self.lineEdit.setText(str(eval(self.lineEdit.text())/100))
            self.phrase_LineEdit.setText(self.phrase_LineEdit.text()+self.lineEdit.text())
        except:
            if self.lineEdit.text() == "":
                pass
            else:
                self.phrase_LineEdit.setText("")
                self.lineEdit.setText("Error")

    def backspace_pressed(self):
        if self.lineEdit.text() == "Error":
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText(self.lineEdit.text()[:-1])
            self.phrase_LineEdit.setText(self.phrase_LineEdit.text()[:-1])

    def clearEntry_pressed(self):
        self.phrase_LineEdit.setText(self.phrase_LineEdit.text()[:-len(self.lineEdit.text())])
        self.lineEdit.setText("")

    def clear_pressed(self):
        self.lineEdit.setText("")
        self.phrase_LineEdit.setText("")
    
    def devisionByx_pressed(self):
        try:
            self.lineEdit.setText(str(1/float(self.lineEdit.text())))
            self.phrase_LineEdit.setText(self.lineEdit.text())
        except:
            if self.lineEdit.text() == "":
                pass
            else:
                self.phrase_LineEdit.setText("")
                self.lineEdit.setText("Error")

    def claculate(self):
        try:
            result = ""
            for i in self.phrase_LineEdit.text():
                if i=="×":
                    result = result+"*"
                elif i=="÷":
                    result = result+"/"
                elif i=="^":
                    result = result+"**"
                else:
                    result = result+i
            self.lineEdit.setText(str(eval(result)))
            self.phrase_LineEdit.setText(str(eval(result)))
        
        except:
            if self.lineEdit.text() == "":
                pass
            else:
                self.phrase_LineEdit.setText("")
                self.lineEdit.setText("Error")
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())