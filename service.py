from flask import Flask
from ask import Request

app = Flask(__name__)


@app.route("/")
def handle_ask_request():
    

if __name__ == "__main__":
    app.run()
