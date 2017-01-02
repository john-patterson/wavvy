__all__ = ['Thermostat']


class Thermostat:
    def __init__(self):
        self.room_temperature = 70.0

    def room_temp(self):
        return self.room_temperature

    def adjust_temp(self, temperature):
        if temperature < 0:
            return False
        self.room_temperature = float(temperature)
        return True
