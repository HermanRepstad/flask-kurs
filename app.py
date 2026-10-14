
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    elevnavn = "Herman"
    return render_template("index.html", 
                           navn = "Herman",
                           klasse = "2IMI",
                           fag = "IM")

@app.route("/om")
def profil():
    return render_template("om.html",
                           navn = "Herman",
                           alder = 16,
                           favorittspråk = "Norsk",
                           skole = "Kuben")

@app.route("/poeng")
def poeng():
    return render_template("poeng.html", poeng = 10)


if __name__ == "__main__":
    app.run(debug = True)   

    