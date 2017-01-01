__all__ = ['Thermostat']

class Thermostat:
    def __init__(self):
        self.room_tempurature = 70.0

    def room_temp(self):
        return self.room_tempurature

    def adjust_temp(self, tempurature):
        self.room_tempurature = tempurature
