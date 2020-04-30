from flask import Flask
from routes.handlers import handlers
from config import config

def runServer():
    app = Flask(__name__)
    app.register_blueprint(handlers)
    app.run(host='0.0.0.0', debug=False, port=config['Server']['port'])


# if __name__ == "__main__":
#     runServer()


