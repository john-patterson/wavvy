from wavvy import thermostat, app, weather, user
from wavvy.datalayer import adjust

__all__ = ['current_room_temp', 'adjust_temp', 'current_outside_temp']

def kelvin_to_fahrenheit(k):
    return (9 / 5) * (k - 273) + 32


def fahrenheit_to_celcius(f):
    return (5 / 9) * (f - 32)


def celcius_to_fahrenheit(c):
    return (9 / 5) * c + 32


def current_room_temp():
    return celcius_to_fahrenheit(thermostat.room_temp())


def current_outside_temp():
    outside = weather.kelvin_by_zip('70501')
    outside = kelvin_to_fahrenheit(outside)
    return outside


def adjust_temp(new_temp):
    new_temp = fahrenheit_to_celcius(float(new_temp))
    outside = current_outside_temp()
    adjust(
        new=float(new_temp),
        outside=outside,
        room=thermostat.room_temp(),
        username=user.current_user())
    thermostat.adjust_temp(new_temp)
