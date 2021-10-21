import Vaccine_Tracker, GUI
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
import sys


#Mandatory: IDNum, thermostatName, address, lot, expiration, remaining
vt1 = Vaccine_Tracker.Vaccine_Tracker(
    IDNum = '1',
    Name = 'Thermostat-Pfizer-Maryland',
    address = 'Maryland',
    lot = '72435',
    expiration = '1/21/25',
    remaining = '773'
)

vt2 = Vaccine_Tracker.Vaccine_Tracker(
    IDNum = '2',
    Name = 'Thermostat-Pfizer-Israel',
    address = 'Maryland',
    lot = '132432',
    expiration = '2/21/25',
    remaining = '773'
)

vt3 = Vaccine_Tracker.Vaccine_Tracker(
    IDNum = '3',
    Name = 'Thermostat-Moderna-Maryland',
    address = 'Maryland',
    lot = '345753',
    expiration = '3/21/25',
    remaining = '773'
)

vt4 = Vaccine_Tracker.Vaccine_Tracker(
    IDNum = '4',
    Name = 'Thermostat-Moderna-Israel',
    address = 'Maryland',
    lot = '685865',
    expiration = '4/21/25',
    remaining = '773'
)

vt5 = Vaccine_Tracker.Vaccine_Tracker(
    IDNum = '5',
    Name = 'Thermostat-JJ-Maryland',
    address = 'Maryland',
    lot = '12870',
    expiration = '5/21/25',
    remaining = '773'
)

vts = [vt1, vt2, vt3, vt4, vt5]

#build connections

#run checks for messages from pubsub to update GUI
#run checks for requests from GUI to build publishes

app = QApplication(sys.argv)

#Styling 

app.setStyle('Fusion')
palette = QPalette()
#Color of the background behind widgets
palette.setColor(QPalette.ColorRole.Window, QColor(128,128,128))
#Text inside the the text boxes
palette.setColor(QPalette.ColorRole.Text, QColor(255,255,255))
#Color of the background of the text boxes
palette.setColor(QPalette.ColorRole.Base, QColor(128,128,128))
#Background color of the button
palette.setColor(QPalette.ColorRole.Button, QColor(255,0,0))
#Color of the text on the button
palette.setColor(QPalette.ColorRole.ButtonText, QColor(255,255,255))
#Text inside the base window
palette.setColor(QPalette.ColorRole.WindowText, QColor(255,255,255))
app.setPalette(palette)
app.setStyleSheet('''
    QWidget {
        font-size: 25px
    }

    QPushButton {
        font-size: 20px
    }
''')

window = GUI.Terra(vts)
window.show()

app.exec()