import Vaccine_Tracker
from typing import Set
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt
import sys, os

class Terra(QMainWindow):

    def __init__(self, vts):
        super(Terra, self).__init__()

        self.setWindowTitle("Terra")
        self.setWindowIcon(QIcon(os.path.join(sys.path[0], 'Photos/Terra.png')))
        self.setMinimumSize(650,450)

        self.vts = vts

        self.vt = Vaccine_Tracker.Vaccine_Tracker(
            IDNum = '--',
            Name = '--',
            address = '--',
            lot = '--',
            expiration = '--',
            remaining = '--'
        )


        FridgeInfoLayout = QVBoxLayout()
        SetFunctionLayout = QVBoxLayout()
        DatabaseInfoLayout = QVBoxLayout()
        DataLayout = QHBoxLayout()
        TopLabelLayout = QHBoxLayout()
        MainLayout = QVBoxLayout()
        BottomLabelLayout = QHBoxLayout()



        #Top Label Layout
        self.IDLabel = QLabel(f'ID: {self.vt.IDNum}')
        self.IDLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.VaccineLabel = QLabel(f'{self.vt.CleanName}')
        self.VaccineLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.AddressLabel = QLabel(f'{self.vt.address}')
        self.AddressLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        TopLabelLayout.addWidget(self.IDLabel)
        TopLabelLayout.addWidget(self.VaccineLabel)
        TopLabelLayout.addWidget(self.AddressLabel)


        #Fridge Info Layout
        FridgeIcon = QLabel()
        FridgeIcon.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/Fridge.png')))
        FridgeIcon.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        TempLabel = QLabel('Temperature')
        TempLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Temperature = QLabel(f'{self.vt.temperature}')
        self.Temperature.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        HumLabel = QLabel('Humidity')
        HumLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Humidity = QLabel(f'{self.vt.humidity}')
        self.Humidity.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        LightLabel = QLabel('Light Status')
        LightLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Light = QLabel()
        if (self.vt.light == 1):
            self.Light.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/LightOn.png')))
        elif (self.vt.light == 0):
            self.Light.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/LightOff.png')))
        self.Light.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        FridgeInfoLayout.addWidget(FridgeIcon)
        FridgeInfoLayout.addWidget(TempLabel)
        FridgeInfoLayout.addWidget(self.Temperature)
        FridgeInfoLayout.addWidget(HumLabel)
        FridgeInfoLayout.addWidget(self.Humidity)
        FridgeInfoLayout.addWidget(LightLabel)
        FridgeInfoLayout.addWidget(self.Light)


        #Set Function Layout
        self.DialLabel = QLabel('--')
        self.DialLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        TempDial = QDial()
        TempDial.setRange(-10, 100)
        TempDial.setSingleStep(0.5)
        TempDial.valueChanged.connect(self.value_changed)
        SetButton = QPushButton('Set')
        LightButtonLabel = QLabel('Fridge Light')
        LightButtonLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        ButtonLayout = QHBoxLayout()
        OnButton = QPushButton('On')
        OnButton.clicked.connect(lambda:self.light_switch(vt, 1))
        OffButton = QPushButton('Off')
        OffButton.clicked.connect(lambda:self.light_switch(vt, 0))
        ButtonLayout.addWidget(OnButton)
        ButtonLayout.addWidget(OffButton)
        SetFunctionLayout.addWidget(TempDial)
        SetFunctionLayout.addWidget(self.DialLabel)
        SetFunctionLayout.addWidget(SetButton, alignment=Qt.AlignmentFlag.AlignTop)
        SetFunctionLayout.addWidget(LightButtonLabel)
        SetFunctionLayout.addLayout(ButtonLayout)


        #Database Info Layout
        VaccineIcon = QLabel()
        VaccineIcon.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/Vaccine.png')))
        VaccineIcon.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        LotLabel = QLabel('Lot #')
        LotLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Lot = QLabel(f'{self.vt.lot}')
        self.Lot.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        ExpLabel = QLabel('Expiration')
        ExpLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Expiration = QLabel(f'{self.vt.expiration}')
        self.Expiration.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        RemainingLabel = QLabel('Remaining Doses')
        RemainingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Remaining = QLabel(f'{self.vt.remaining}')
        self.Remaining.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        DatabaseInfoLayout.addWidget(VaccineIcon)
        DatabaseInfoLayout.addWidget(LotLabel)
        DatabaseInfoLayout.addWidget(self.Lot)
        DatabaseInfoLayout.addWidget(ExpLabel)
        DatabaseInfoLayout.addWidget(self.Expiration)
        DatabaseInfoLayout.addWidget(RemainingLabel)
        DatabaseInfoLayout.addWidget(self.Remaining)

        #Bottom Label Layout
        self.LastMessageLabel = QLabel(f'Last Update: {self.vt.lastUpdate}')
        self.LastMessageLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        forceUpdateButton = QPushButton('Force Update')
        BottomLabelLayout.addWidget(self.LastMessageLabel)
        BottomLabelLayout.addWidget(forceUpdateButton, alignment=Qt.AlignmentFlag.AlignLeft)

        ##Main Layout
        MainLayout.addLayout(TopLabelLayout)
        MainLayout.addLayout(DataLayout)
        MainLayout.addLayout(BottomLabelLayout)

        #Data Layout 
        DataLayout.addLayout(FridgeInfoLayout)
        DataLayout.addLayout(SetFunctionLayout)
        DataLayout.addLayout(DatabaseInfoLayout)

        #Create Menu
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)
        fileMenu = QMenu('&Change Tab', self)

        VTMenu = []
        index = 0

        for vt in vts:
            VTMenu.append(QAction(f'&VT{vt.IDNum}', self))
            VTMenu[index].triggered.connect(lambda:self.switch_page(index))
            fileMenu.addAction(VTMenu[index])
            index += 1

        # index = 0

        # for item in VTMenu:
        #     test = vtObject[index]
        #     item.triggered.connect(self.switch_page(test))
        #     index += 1

        exitAct = QAction('&Exit', self)
        exitAct.triggered.connect(QApplication.instance().quit)
        fileMenu.addAction(exitAct)

        menuBar.addMenu(fileMenu) 

        widget = QWidget()
        widget.setLayout(MainLayout)
        self.setCentralWidget(widget)

    def value_changed(self, i):
        self.DialLabel.setText(str(i))

    def light_switch(self, vt, i):
        vt.light = i
        update_GUI(self, vt)

    def switch_page(self, index):
        self.vt = self.vts[index]
        update_GUI(self, self.vt)


def update_GUI(self, vt):
    self.IDLabel = QLabel(f'ID: {vt.IDNum}')
    self.VaccineLabel = QLabel(f'{vt.CleanName}')
    self.AddressLabel = QLabel(f'{vt.address}')
    self.Temperature = QLabel(f'{vt.temperature}')
    self.Humidity = QLabel(f'{vt.humidity}')
    if (vt.light == 1):
        self.Light.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/LightOn.png')))
    elif (vt.light == 0):
        self.Light.setPixmap(QPixmap(os.path.join(sys.path[0], 'Photos/LightOff.png')))
    self.Lot = QLabel(f'{vt.lot}')
    self.Expiration = QLabel(f'{vt.expiration}')
    self.Remaining = QLabel(f'{vt.remaining}')

      