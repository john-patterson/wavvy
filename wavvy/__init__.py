from flask import Flask

app = Flask(__name__)
app.secret_key = 'spooky'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'

import wavvy.views
import wavvy.datalayer
