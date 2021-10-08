import Thermostat, GUI
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
import sys


#Mandatory: IDNum, thermostatName, address, lot, expiration, remaining
thermostat = Thermostat.Thermostat(
    IDNum = '1',
    thermostatName = 'Thermostat-Pfizer-Maryland',
    address = 'Maryland',
    lot = '72435',
    expiration = '7/21/25',
    remaining = '773'
)

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

window = GUI.Terra(thermostat)
window.show()

app.exec()