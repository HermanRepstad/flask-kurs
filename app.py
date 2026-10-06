
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Velkomme til min førte flask app"


if __name__ == "__main__":
    app.run(debug = True)   