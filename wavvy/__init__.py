from flask import Flask

app = Flask(__name__)
app.secret_key = 'spooky'

import wavvy.views
