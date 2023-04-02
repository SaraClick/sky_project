from flask import Flask

# Instantiate Flask application
app = Flask(__name__)

# Import the routes file code to make sure that Flask knows the routes of our project
# MUST be after app = Flask(__name__) otherwise we will get an error!
from application import routes
