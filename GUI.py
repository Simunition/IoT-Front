from Thermostat import Thermostat
from typing import Set
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import QSize, Qt
import sys

class Terra(QMainWindow):

    def __init__(self, thermostat):
        super(Terra, self).__init__()

        self.setWindowTitle("Terra")
        self.setWindowIcon(QIcon('Terra.png'))
        self.setMinimumSize(650,450)

        FridgeInfoLayout = QVBoxLayout()
        SetFunctionLayout = QVBoxLayout()
        DatabaseInfoLayout = QVBoxLayout()
        DataLayout = QHBoxLayout()
        TopLabelLayout = QHBoxLayout()
        MainLayout = QVBoxLayout()
        BottomLabelLayout = QHBoxLayout()



        #Top Label Layout
        self.IDLabel = QLabel(f'ID: {thermostat.IDNum}')
        self.IDLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.VaccineLabel = QLabel(f'{thermostat.thermostatName}')
        self.VaccineLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.AddressLabel = QLabel(f'{thermostat.address}')
        self.AddressLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        TopLabelLayout.addWidget(self.IDLabel)
        TopLabelLayout.addWidget(self.VaccineLabel)
        TopLabelLayout.addWidget(self.AddressLabel)


        #Fridge Info Layout
        FridgeIcon = QLabel()
        FridgeIcon.setPixmap(QPixmap('Fridge.png'))
        FridgeIcon.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        TempLabel = QLabel('Temperature')
        TempLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Temperature = QLabel(f'{thermostat.temperature}')
        self.Temperature.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        HumLabel = QLabel('Humidity')
        HumLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Humidity = QLabel(f'{thermostat.humidity}')
        self.Humidity.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        LightLabel = QLabel('Light Status')
        LightLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Light = QLabel()
        if (thermostat.light == 1):
            self.Light.setPixmap(QPixmap('LightOn.png'))
        elif (thermostat.light == 0):
            self.Light.setPixmap(QPixmap('LightOff.png'))
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
        OnButton.clicked.connect(lambda:self.light_switch(thermostat, 1))
        OffButton = QPushButton('Off')
        OffButton.clicked.connect(lambda:self.light_switch(thermostat, 0))
        ButtonLayout.addWidget(OnButton)
        ButtonLayout.addWidget(OffButton)
        SetFunctionLayout.addWidget(TempDial)
        SetFunctionLayout.addWidget(self.DialLabel)
        SetFunctionLayout.addWidget(SetButton, alignment=Qt.AlignmentFlag.AlignTop)
        SetFunctionLayout.addWidget(LightButtonLabel)
        SetFunctionLayout.addLayout(ButtonLayout)


        #Database Info Layout
        VaccineIcon = QLabel()
        VaccineIcon.setPixmap(QPixmap('Vaccine.png'))
        VaccineIcon.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        LotLabel = QLabel('Lot #')
        LotLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Lot = QLabel(f'{thermostat.lot}')
        self.Lot.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        ExpLabel = QLabel('Expiration')
        ExpLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Expiration = QLabel(f'{thermostat.expiration}')
        self.Expiration.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        RemainingLabel = QLabel('Remaining Doses')
        RemainingLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.Remaining = QLabel(f'{thermostat.remaining}')
        self.Remaining.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        DatabaseInfoLayout.addWidget(VaccineIcon)
        DatabaseInfoLayout.addWidget(LotLabel)
        DatabaseInfoLayout.addWidget(self.Lot)
        DatabaseInfoLayout.addWidget(ExpLabel)
        DatabaseInfoLayout.addWidget(self.Expiration)
        DatabaseInfoLayout.addWidget(RemainingLabel)
        DatabaseInfoLayout.addWidget(self.Remaining)

        #Bottom Label Layout
        self.LastMessageLabel = QLabel(f'Last Update: {thermostat.lastUpdate}')
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

        widget = QWidget()
        widget.setLayout(MainLayout)
        self.setCentralWidget(widget)

    def value_changed(self, i):
        self.DialLabel.setText(str(i))

    def light_switch(self, thermostat, i):
        thermostat.light = i
        update_GUI(self, thermostat)

def update_GUI(self, thermostat):
    self.IDLabel = QLabel(f'ID: {thermostat.IDNum}')
    self.VaccineLabel = QLabel(f'{thermostat.thermostatName}')
    self.AddressLabel = QLabel(f'{thermostat.address}')
    self.Temperature = QLabel(f'{thermostat.temperature}')
    self.Humidity = QLabel(f'{thermostat.humidity}')
    if (thermostat.light == 1):
        self.Light.setPixmap(QPixmap('LightOn.png'))
    elif (thermostat.light == 0):
        self.Light.setPixmap(QPixmap('LightOff.png'))
    self.Lot = QLabel(f'{thermostat.lot}')
    self.Expiration = QLabel(f'{thermostat.expiration}')
    self.Remaining = QLabel(f'{thermostat.remaining}')

        