from flask import send_from_directory, send_file
from flask_app import app
from flask.templating import render_template

# Routing voor de Nederlandstalige pagina's.
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/nieuws')
def nieuws():
    return render_template("nieuws.html")

@app.route('/nieuws/<nb>')
def nieuwsitem(nb):
    return render_template("nieuws/nieuwsitem" + nb + ".html")

@app.route('/dojo/info')
def info():
    return render_template("dojo/info.html")


@app.route('/dojo/kalender')
def kalender():
    return render_template("dojo/kalender.html")


@app.route('/kyokushin/geschiedenis')
def geschiedenis():
    return render_template("kyokushin/geschiedenis.html")


@app.route('/kyokushin/spirit')
def spirit():
    return render_template("kyokushin/spirit.html")

@app.route('/kyokushin/kihon')
def kihon():
    return render_template("kyokushin/kihon.html")


@app.route('/kyokushin/kata')
def kata():
    return render_template("kyokushin/kata.html")


@app.route('/kyokushin/kumite')
def kumite():
    return render_template("kyokushin/kumite.html")


@app.route('/links')
def links():
    return render_template("links.html")