import os

from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ['WAVVY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import wavvy.views
import wavvy.datalayer

config = {
    'owm-key': os.environ['WEATHER_API_KEY']
}

weather = wavvy.datalayer.weather.OpenWeather(config['owm-key'])
thermostat = wavvy.datalayer.wave.Thermostat()
