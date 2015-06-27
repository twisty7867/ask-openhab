from flask import Flask
from ask import Request

app = Flask(__name__)


@app.route("/ask-openhab")
def handle_ask_request():
    r = request.get_json()
    print r
    return


if __name__ == "__main__":
    app.run()