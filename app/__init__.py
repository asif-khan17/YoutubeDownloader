from flask import Flask
import config
from routes import routes



app = Flask(__name__)
app.config.from_object(config.DevConfig)


app.register_blueprint(routes, url_prefix="/api")