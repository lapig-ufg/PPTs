from PyQt5 import QtGui, QtPrintSupport , QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QDesktopWidget, QFileDialog, QTextEdit
from PyQt5.QtCore import QCoreApplication
import sys
import os
import datetime
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GPM_WINDOW(object):

    def setupUi(self, GPM_WINDOW):

        End_Date = list(map(int,((datetime.datetime.now()).strftime('%Y-%m-%d')).split('-')))
        Year = int(End_Date[0])
        Month = int(End_Date[1])
        Day = int(End_Date[2])


        GPM_WINDOW.setObjectName("GPM_WINDOW")
        GPM_WINDOW.setWindowModality(QtCore.Qt.NonModal)
        GPM_WINDOW.setEnabled(True)
        GPM_WINDOW.resize(350, 449)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GPM_WINDOW.sizePolicy().hasHeightForWidth())
        GPM_WINDOW.setSizePolicy(sizePolicy)
        GPM_WINDOW.setMinimumSize(QtCore.QSize(350, 410))
        GPM_WINDOW.setMaximumSize(QtCore.QSize(1920, 1080))
        GPM_WINDOW.setSizeIncrement(QtCore.QSize(0, 0))
        GPM_WINDOW.setBaseSize(QtCore.QSize(350, 350))
        self.GPM_Window = QtWidgets.QWidget(GPM_WINDOW)
        self.GPM_Window.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.GPM_Window.setObjectName("GPM_Window")
        

        #SPATIAL SLICE
        self.Global_Slice_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self.Global_Slice_BT.setGeometry(QtCore.QRect(10, 200, 82, 17))
        self.Global_Slice_BT.setChecked(True)
        self.Global_Slice_BT.setObjectName("Global_Slice_BT")
        
        self.ScaleSlice = QtWidgets.QButtonGroup(GPM_WINDOW)
        self.ScaleSlice.setObjectName("ScaleSlice")
        self.ScaleSlice.addButton(self.Global_Slice_BT)
        
        self.Regional_Slice_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self.Regional_Slice_BT.setGeometry(QtCore.QRect(10, 220, 82, 17))
        self.Regional_Slice_BT.setChecked(False)
        self.Regional_Slice_BT.setObjectName("Regional_Slice_BT")
        ##
        self.Regional_Slice_BT.toggled.connect(lambda:self.CheckCheck(self.Regional_Slice_BT))
        
        self.ScaleSlice.addButton(self.Regional_Slice_BT)
        self.Mask_Insert_BT = QtWidgets.QToolButton(self.GPM_Window)
        self.Mask_Insert_BT.setEnabled(False)
        self.Mask_Insert_BT.setGeometry(QtCore.QRect(30, 260, 51, 21))
        self.Mask_Insert_BT.setCheckable(False)
        self.Mask_Insert_BT.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.Mask_Insert_BT.setArrowType(QtCore.Qt.RightArrow)
        self.Mask_Insert_BT.setObjectName("Mask_Insert_BT")
        self.Mask_Insert_BT.clicked.connect(self.selectSlice)
        #self.ScaleSlice.addButton(self.Mask_Insert_BT)
  
        self.Mask_Insert_LB = QtWidgets.QLabel(self.GPM_Window)
        self.Mask_Insert_LB.setGeometry(QtCore.QRect(30, 240, 111, 16))
        self.Mask_Insert_LB.setObjectName("Mask_Insert_LB")

        self.Spatial_Slice_LB = QtWidgets.QLabel(self.GPM_Window)
        self.Spatial_Slice_LB.setGeometry(QtCore.QRect(10, 180, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Spatial_Slice_LB.setFont(font)
        self.Spatial_Slice_LB.setObjectName("Spatial_Slice_LB")

        self.MaskDir_TX = QtWidgets.QLineEdit(self.GPM_Window)
        self.MaskDir_TX.setEnabled(False)
        self.MaskDir_TX.setGeometry(QtCore.QRect(90, 260, 221, 20))
        self.MaskDir_TX.setObjectName("MaskDir_TX")

        #TEMPORAL SLICE    
        self.Start_Date_Cal = QtWidgets.QDateEdit(self.GPM_Window)
        self.Start_Date_Cal.setGeometry(QtCore.QRect(70, 100, 81, 22))
        self.Start_Date_Cal.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1998, 1, 1), QtCore.QTime(0, 0, 0)))
        self.Start_Date_Cal.setCalendarPopup(True)
        self.Start_Date_Cal.setDate(QtCore.QDate(2014, 3, 12))
        self.Start_Date_Cal.setObjectName("Start_Date_Cal")
        
        self.D_M_Y_LB1 = QtWidgets.QLabel(self.GPM_Window)
        self.D_M_Y_LB1.setGeometry(QtCore.QRect(70, 80, 81, 16))
        self.D_M_Y_LB1.setObjectName("D_M_Y_LB1")
        
        self.Start_Date_LB = QtWidgets.QLabel(self.GPM_Window)
        self.Start_Date_LB.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.Start_Date_LB.setObjectName("Start_Date_LB")
        
        self.End_Date_Cal = QtWidgets.QDateEdit(self.GPM_Window)
        self.End_Date_Cal.setGeometry(QtCore.QRect(70, 150, 81, 22))
        self.End_Date_Cal.setProperty("showGroupSeparator", False)
        self.End_Date_Cal.setCalendarPopup(True)
        self.End_Date_Cal.setDate(QtCore.QDate(Year, Month, Day))
        self.End_Date_Cal.setObjectName("End_Date_Cal")
        
        self.D_M_Y_LB2 = QtWidgets.QLabel(self.GPM_Window)
        self.D_M_Y_LB2.setGeometry(QtCore.QRect(70, 130, 81, 16))
        self.D_M_Y_LB2.setObjectName("D_M_Y_LB2")
       
        self.End_Date_LB = QtWidgets.QLabel(self.GPM_Window)
        self.End_Date_LB.setGeometry(QtCore.QRect(10, 150, 51, 16))
        self.End_Date_LB.setObjectName("End_Date_LB")



        #PRODUCT TYPE        
        self.GPM_M_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self.GPM_M_BT.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.GPM_M_BT.setChecked(True)
        self.GPM_M_BT.setObjectName("GPM_M_BT")
        
        self.Precipitation_Products = QtWidgets.QButtonGroup(GPM_WINDOW)
        self.Precipitation_Products.setObjectName("Precipitation_Products")
        self.Precipitation_Products.addButton(self.GPM_M_BT)
        self.GPM_D_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self.GPM_D_BT.setGeometry(QtCore.QRect(90, 30, 82, 17))
        self.GPM_D_BT.setObjectName("GPM_D_BT")
        self.Precipitation_Products.addButton(self.GPM_D_BT)
        self._TRMM_M_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self._TRMM_M_BT.setGeometry(QtCore.QRect(160, 30, 82, 17))
        self._TRMM_M_BT.setObjectName("_TRMM_M_BT")
        self.Precipitation_Products.addButton(self._TRMM_M_BT)
        self.TRMM_D_BT = QtWidgets.QRadioButton(self.GPM_Window)
        self.TRMM_D_BT.setGeometry(QtCore.QRect(250, 30, 82, 17))
        self.TRMM_D_BT.setObjectName("TRMM_D_BT")
        self.Precipitation_Products.addButton(self.TRMM_D_BT)
        
        #PRODUCT CHECKS

        self.GPM_M_BT.toggled.connect(lambda:self.CheckProd(self.GPM_M_BT))
        self.GPM_D_BT.toggled.connect(lambda:self.CheckProd(self.GPM_D_BT))
        self._TRMM_M_BT.toggled.connect(lambda:self.CheckProd(self._TRMM_M_BT))
        self.TRMM_D_BT.toggled.connect(lambda:self.CheckProd(self.TRMM_D_BT))


        self.PPT_TypeLb = QtWidgets.QLabel(self.GPM_Window)
        self.PPT_TypeLb.setGeometry(QtCore.QRect(10, 10, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PPT_TypeLb.setFont(font)
        self.PPT_TypeLb.setObjectName("PPT_TypeLb")
 
        self.Date_Slice_LB = QtWidgets.QLabel(self.GPM_Window)
        self.Date_Slice_LB.setGeometry(QtCore.QRect(10, 60, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Date_Slice_LB.setFont(font)
        self.Date_Slice_LB.setObjectName("Date_Slice_LB")
        
        self.DW_PC_DIR_LB = QtWidgets.QLabel(self.GPM_Window)
        self.DW_PC_DIR_LB.setGeometry(QtCore.QRect(10, 290, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DW_PC_DIR_LB.setFont(font)
        self.DW_PC_DIR_LB.setObjectName("DW_PC_DIR_LB")
        
        self.OutDir_BT = QtWidgets.QToolButton(self.GPM_Window)
        self.OutDir_BT.setGeometry(QtCore.QRect(30, 310, 51, 21))
        self.OutDir_BT.setCheckable(False)
        self.OutDir_BT.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.OutDir_BT.setArrowType(QtCore.Qt.RightArrow)
        self.OutDir_BT.setObjectName("OutDir_BT")

        #self.myTextBox = QtWidgets.QTextEdit()
        self.window = GPM_WINDOW
        self.OutDir_BT.clicked.connect(self.selectOUT)

        self.OutDir_TX = QtWidgets.QLineEdit(self.GPM_Window)
        self.OutDir_TX.setGeometry(QtCore.QRect(90, 310, 221, 20))
        self.OutDir_TX.setObjectName("OutDir_TX")
        
   
        #PHOTOS
        self.label = QtWidgets.QLabel(self.GPM_Window)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(160, 60, 181, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gpm_1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        #STATUSBAR
        self.statusbar = QtWidgets.QStatusBar(GPM_WINDOW)
        self.statusbar.setObjectName("statusbar")
     
        #RUN EXIT BUTTONS
        self.Run_BT = QtWidgets.QPushButton(self.GPM_Window)
        self.Run_BT.setGeometry(QtCore.QRect(90, 360, 75, 23))
        self.Run_BT.setObjectName("Run_BT")
        self.Run_BT.clicked.connect(self.exec_Processing)
        
        self.Exit_BT = QtWidgets.QPushButton(self.GPM_Window)
        self.Exit_BT.setGeometry(QtCore.QRect(180, 360, 75, 23))
        self.Exit_BT.setObjectName("Exit_BT")
        self.Exit_BT.clicked.connect(QCoreApplication.instance().quit)

        self.OP_BT = QtWidgets.QCheckBox(self.GPM_Window)
        self.OP_BT.setGeometry(QtCore.QRect(10, 390, 81, 21))
        self.OP_BT.setObjectName("OP_BT")
        self.OP_LB = QtWidgets.QLabel(self.GPM_Window)
        self.OP_LB.setGeometry(QtCore.QRect(10, 410, 271, 21))
        self.OP_LB.setObjectName("OP_LB")


        self.retranslateUi(GPM_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(GPM_WINDOW)

    def retranslateUi(self, GPM_WINDOW,):
        _translate = QtCore.QCoreApplication.translate
        GPM_WINDOW.setWindowTitle(_translate("GPM_WINDOW", "Precipitation Processing Tools"))
        self.Global_Slice_BT.setText(_translate("GPM_WINDOW", "Global"))
        self.Regional_Slice_BT.setText(_translate("GPM_WINDOW", "Regional slice"))
        self.Mask_Insert_BT.setText(_translate("GPM_WINDOW", "..."))
        self.Mask_Insert_LB.setText(_translate("GPM_WINDOW", "Insert the slice mask:"))
        self.D_M_Y_LB1.setText(_translate("GPM_WINDOW", "Day/Month/Year"))
        self.Start_Date_LB.setText(_translate("GPM_WINDOW", "Start Date:"))
        self.D_M_Y_LB2.setText(_translate("GPM_WINDOW", "Day/Month/Year"))
        self.End_Date_LB.setText(_translate("GPM_WINDOW", "End Date:"))
        self.GPM_M_BT.setText(_translate("GPM_WINDOW", "GPM Month"))
        self.GPM_D_BT.setText(_translate("GPM_WINDOW", "GPM Day"))
        self._TRMM_M_BT.setText(_translate("GPM_WINDOW", "TRMM Month"))
        self.TRMM_D_BT.setText(_translate("GPM_WINDOW", "TRMM Day"))
        self.PPT_TypeLb.setText(_translate("GPM_WINDOW", "Precipitation Product type:"))
        self.Date_Slice_LB.setText(_translate("GPM_WINDOW", "Date slice:"))
        self.Spatial_Slice_LB.setText(_translate("GPM_WINDOW", "Spatial slice:"))
        self.DW_PC_DIR_LB.setText(_translate("GPM_WINDOW", "Download and Processing directory:"))
        self.OutDir_BT.setText(_translate("GPM_WINDOW", "..."))
        self.OutDir_TX.setText(_translate("GPM_WINDOW", ''))
        self.MaskDir_TX.setText(_translate("GPM_WINDOW", ''))
        self.Run_BT.setText(_translate("GPM_WINDOW", "Run"))
        self.Exit_BT.setText(_translate("GPM_WINDOW", "Close"))
        self.OP_BT.setText(_translate("GPM_WINDOW", "Only Process"))
        self.OP_LB.setText(_translate("GPM_WINDOW", "(Mark this only if you wanna process downloaded data)"))

    def selectOUT(self):
        outdir = QFileDialog.getExistingDirectory(self.window, 'Select the download and/or processing directory', os.getenv('HOME'))
        outdir_txt = r'%s' % str(outdir);
        self.OutDir_TX.setText(outdir_txt)

    def selectSlice(self):
        dataMask = QFileDialog.getOpenFileName(self.window, 'Select the data you want to use like mask (Shapefiles ONLY!!!!)', os.getenv('HOME'),"ESRI Shapefile (*.shp)")
        dataMask_txt = r'%s' % str(dataMask[0]);
        self.MaskDir_TX.setText(dataMask_txt)
        #return()
    def CheckCheck(self,b):
            if b.isChecked() == True:
                self.Global_Slice_BT.setChecked(False)
                self.Mask_Insert_BT.setEnabled(True)
                self.Mask_Insert_BT.setCheckable(True)
                self.MaskDir_TX.setEnabled(True)
            else:
                self.Global_Slice_BT.setChecked(True)
                self.Mask_Insert_BT.setEnabled(False)
                self.Mask_Insert_BT.setCheckable(False)
                self.MaskDir_TX.setEnabled(False)
                self.MaskDir_TX.setText('')

    def CheckProd(self,a):
        
        DateNow = list(map(int,((datetime.datetime.now()).strftime('%Y-%m-%d')).split('-')))
        YearNow = int(DateNow[0])
        MonthNow = int(DateNow[1])
        DayNow = int(DateNow[2])

        if a.isChecked() == True and a.text() == "GPM Month":
            self.Start_Date_Cal.setDate(QtCore.QDate(2014, 3, 12))
            self.End_Date_Cal.setDate(QtCore.QDate(YearNow, MonthNow, DayNow))

        elif a.isChecked() == True and a.text() == "GPM Day":
            self.Start_Date_Cal.setDate(QtCore.QDate(2014, 3, 12))
            self.End_Date_Cal.setDate(QtCore.QDate(YearNow, MonthNow, DayNow))

        elif a.isChecked() == True and a.text() == "TRMM Month":
            self.Start_Date_Cal.setDate(QtCore.QDate(1998, 1, 1))
            self.End_Date_Cal.setDate(QtCore.QDate(YearNow, MonthNow, DayNow))
        
        elif a.isChecked() == True and a.text() == "TRMM Day":
            self.Start_Date_Cal.setDate(QtCore.QDate(1998, 1, 1))
            self.End_Date_Cal.setDate(QtCore.QDate(YearNow, MonthNow, DayNow))
        
        else:
            pass

    def exec_Processing(self):
        ProdTp = None

        if self.GPM_M_BT.isChecked() == True and self.GPM_M_BT.text() == "GPM Month":
            ProdTp = 'GPM_M'
        elif self.GPM_D_BT.isChecked() == True and self.GPM_D_BT.text() == "GPM Day":
            ProdTp = 'GPM_D'
        elif self._TRMM_M_BT.isChecked() == True and self._TRMM_M_BT.text() == "TRMM Month":
            ProdTp = 'TRMM_M'
        elif self.TRMM_D_BT.isChecked() == True and self.TRMM_D_BT.text() == "TRMM Day":
            ProdTp = 'TRMM_D'
        else:
            pass

        OP_Info = ''
        if self.OP_BT.isChecked() == True:
            OP_Info = '--OP'

        StartDate = str((datetime.datetime.strptime(str(self.Start_Date_Cal.text()),'%d/%M/%Y')).strftime('%Y-%M-%d'))
        EndDate = str((datetime.datetime.strptime(str(self.End_Date_Cal.text()),'%d/%M/%Y')).strftime('%Y-%M-%d'))
        Donwload_Dir = r'%s' % str(self.OutDir_TX.text())
        
        Slice_Dir = r'%s' % str(self.MaskDir_TX.text())
        
        if Slice_Dir == '':
            Slice_Dir = 'None'

        #zz = (ProdTp,StartDate,EndDate,Donwload_Dir,Slice_Dir,OP_Info)
        #print(zz);
        os.system('python Integration.py --ProdTP ' + ProdTp + ' --StartDate ' + StartDate + ' --EndDate ' + EndDate + ' --ProcessDir ' + Donwload_Dir + ' --SptSlc ' + Slice_Dir + ' ' + OP_Info)

if __name__ == "__main__":  

    
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_GPM_WINDOW()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())