
class Thermostat:

    #Attributes for setting and maintaining data about the thermostat and values associated with a typical physical device
    #last humidity and last temp are used to know which direction to move in when psuedo naturally changing those values.

    def __init__(self, IDNum, thermostatName, address, lot, 
                    expiration, remaining, temperature = 70,
                    setTemperature = 70, humidity = 65,
                    light = 0, lastUpdate = "Never"):
        self.IDNum = IDNum
        self.thermostatName = clean_name(thermostatName)
        self.address = address
        self.temperature = temperature
        self.setTemperature = setTemperature
        self.humidity = humidity
        self.light = light
        self.lot = lot
        self.expiration = expiration
        self.remaining = remaining
        self.lastUpdate = lastUpdate

        self.data = {
            "IDNum":self.IDNum,
            "thermostatName":self.thermostatName,
            "address":self.address,
            "temperature":self.temperature,
            "setTemperature":self.setTemperature,
            "humidity":self.humidity,
            "light":self.light,
            "lot":self.lot,
            "expiration":self.expiration,
            "remaining":self.remaining,
            "lastUpdate":self.lastUpdate
        }

    def __str__(self):
        return str(self.data)

def clean_name(thermostatName):
    data = thermostatName.split('-')
    return data[1]

