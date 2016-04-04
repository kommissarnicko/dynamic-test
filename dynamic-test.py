from flask import Flask
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello():
    """Dynamic greeting."""
	time = datetime.now().time()
	greeting = "Nick Williams Site, time now is " + time
    return greeting


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)