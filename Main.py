import Vaccine_Tracker, GUI, Connection_Controller
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
import sys
from awscrt import mqtt, io
from awsiot import mqtt_connection_builder


def main():

    log_file = open('log.txt', 'a')

    #Spin up resources for connection to IoT Core MQTT Broker 

    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

    connection = Connection_Controller.Connection_Controller()

    endpoint = 'a1w7q2emoqb76a-ats.iot.us-east-2.amazonaws.com'   #ex \"abcd12345wxyz-ats.iot.us-east-1.amazonaws.com\"
    port = 8883      #443 or 8883
    cert = '/home/esims/Desktop/Temp/IoT-Front/Credentials/thermostat-certificate.pem.crt'       #file path to client cert in PEM format.
    key = '/home/esims/Desktop/Temp/IoT-Front/Credentials/thermostat-private.pem.key'        #File path to your private key, in PEM format.
    root_ca = '/home/esims/Desktop/Temp/IoT-Front/Credentials/AmazonRootCA1.pem'    #file path to root CA in PEM format.
    client_id = 'Terra'  #client ID for MQTT connection
    sub_topic = 'Thermostats-Feed'      #topic to sub to

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
            endpoint=endpoint,
            port=port,
            cert_filepath=cert,
            pri_key_filepath=key,
            client_bootstrap=client_bootstrap,
            ca_filepath=root_ca,
            on_connection_interrupted=connection.on_connection_interrupted,
            on_connection_resumed=connection.on_connection_resumed,
            client_id=client_id,
            clean_session=False,
            keep_alive_secs=30,
        )

    log_file.write("Connecting to {} with client ID '{}'... \n".format(
        endpoint, client_id))

    connect_future = mqtt_connection.connect()

    #Future.result() waits until a result is available

    connect_future.result()
    log_file.write("Connected!\n")

    log_file.write("Subscribing to topic '{}'...\n".format(sub_topic))
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=sub_topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=connection.on_message_received)

    #Confirmation that subscription was successful 

    subscribe_result = subscribe_future.result()
    log_file.write("Subscribed with {}\n".format(str(subscribe_result['qos'])))

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

    window = GUI.Terra(mqtt_connection)
    window.show()

    #app.exec()

    try:
        app.exec()

    except KeyboardInterrupt:
        #set to run upon application exit
        #disconnect the MQTT broker connection

        log_file.write("Disconnecting...\n")
        log_file.close()
        disconnect_future = mqtt_connection.disconnect()
        disconnect_future.result()
        log_file.write("Disconnected!\n")


if __name__ == "__main__":
    main()