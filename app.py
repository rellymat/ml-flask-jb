from flask import Flask
from handlers.dataroutes import configure
app = Flask(__name__)

configure(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

