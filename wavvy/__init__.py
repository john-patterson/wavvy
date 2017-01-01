import os

from flask import Flask

app = Flask(__name__)
app.secret_key = os.environ['WAVVY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import wavvy.views
import wavvy.datalayer

weather = wavvy.datalayer.OpenWeather(os.environ['WEATHER_API_KEY'])
thermostat = wavvy.datalayer.Thermostat()
