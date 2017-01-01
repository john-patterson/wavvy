import os

from flask import Flask, session

app = Flask(__name__)
app.secret_key = os.environ['WAVVY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config = {
    'owm-key': os.environ['WEATHER_API_KEY']
}


import wavvy.datalayer
weather = wavvy.datalayer.weather.OpenWeather(config['owm-key'])
thermostat = wavvy.datalayer.wave.Thermostat()

from wavvy.auth import Auth
user = Auth(session)


import wavvy.views
