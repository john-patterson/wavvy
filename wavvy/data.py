from wavvy import thermostat, app, weather, user
from wavvy.datalayer import adjust, get_current_setting

__all__ = ['current_room_temp', 'adjust_temp', 'current_outside_temp']

def kelvin_to_fahrenheit(k):
    return (9 / 5) * (k - 273) + 32


def fahrenheit_to_celcius(f):
    return (5 / 9) * (f - 32)


def celcius_to_fahrenheit(c):
    return (9 / 5) * c + 32


def current_setting():
    setting = get_current_setting()
    return celcius_to_fahrenheit(setting) if setting else 'None'

def current_room_temp():
    return celcius_to_fahrenheit(thermostat.room_temp())


def current_outside_temp():
    outside = weather.kelvin_by_zip('70501')
    outside = kelvin_to_fahrenheit(outside)
    return outside


def adjust_temp(new_temp):
    # form is assumed to be Fahrenheit
    new_temp = float(new_temp)
    thermostat.adjust_temp(fahrenheit_to_celcius(new_temp))
    outside = current_outside_temp()
    adjust(
        new=new_temp,
        outside=outside,
        room=thermostat.room_temp(),
        username=user.current_user())
