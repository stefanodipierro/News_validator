from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

# Import configuration settings
# app.config.from_object('app.config')

# Import routes
from app import routes
