from flask_app import app
from flask.templating import render_template

# Routing voor de Nederlandstalige pagina's.
@app.route('/')
@app.route('/index')
@app.route('/nl/index')
def nlIndex():
    return render_template("nl/index.html")


@app.route('/profiel')
@app.route('/nl/profiel')
def nlProfiel():
    return render_template("nl/profiel.html")


@app.route('/instellingen')
@app.route('/nl/instellingen')
def nlInstellingen():
    return render_template("nl/instellingen.html")


@app.route('/nieuws')
@app.route('/nl/nieuws')
def nlNieuws():
    return render_template("nl/nieuws.html")


@app.route('/dojo/oshishinobu')
@app.route('/nl/dojo/oshishinobu')
def nlOshishinobu():
    return render_template("nl/dojo/oshishinobu.html")


@app.route('/dojo/info')
@app.route('/nl/dojo/info')
def nlInfo():
    return render_template("nl/dojo/info.html")


@app.route('/dojo/kalender')
@app.route('/nl/dojo/kalender')
def nlKalender():
    return render_template("nl/dojo/kalender.html")


@app.route('/dojo/fotoalbum')
@app.route('/nl/dojo/fotoalbum')
def nlFotoalbum():
    return render_template("nl/dojo/fotoalbum.html")


@app.route('/dojo/nieuwsbrief')
@app.route('/nl/dojo/nieuwsbrief')
def nlNieuwsbrief():
    return render_template("nl/dojo/nieuwsbrief.pdf")


@app.route('/dojo/syllabus')
@app.route('/nl/dojo/syllabus')
def nlSyllabus():
    return render_template("nl/dojo/syllabus.html")


@app.route('/kyokushin/geschiedenis')
@app.route('/nl/kyokushin/geschiedenis')
def nlGeschiedenis():
    return render_template("nl/kyokushin/geschiedenis.html")


@app.route('/kyokushin/spirit')
@app.route('/nl/kyokushin/spirit')
def nlSpirit():
    return render_template("nl/kyokushin/spirit.html")


@app.route('/kyokushin/opwarming')
@app.route('/nl/kyokushin/opwarming')
def nlOpwarming():
    return render_template("nl/kyokushin/opwarming.html")


@app.route('/kyokushin/kihon')
@app.route('/nl/kyokushin/kihon')
def nlKihon():
    return render_template("nl/kyokushin/kihon.html")


@app.route('/kyokushin/kata')
@app.route('/nl/kyokushin/kata')
def nlKata():
    return render_template("nl/kyokushin/kata.html")


@app.route('/kyokushin/kumite')
@app.route('/nl/kyokushin/kumite')
def nlKumite():
    return render_template("nl/kyokushin/kumite.html")


@app.route('/links')
@app.route('/nl/links')
def nlLinks():
    return render_template("nl/links.html")


# --------------------------------------------------------------------

# Routing voor de Engelstalige pagina's
@app.route('/en/index')
def enIndex():
    return render_template("en/index.html")


@app.route('/dojomanagement')
@app.route('/en/dojomanagement')
def enDojomanagement():
    return render_template("en/dojomanagement.html")


@app.route('/profile')
@app.route('/en/profile')
def enProfile():
    return render_template("en/profile.html")


@app.route('/settings')
@app.route('/en/settings')
def enSettings():
    return render_template("en/settings.html")


@app.route('/en/news')
def enNews():
    return render_template("en/news.html")


@app.route('/en/dojo/oshishinobu')
def enOshishinobu():
    return render_template("en/dojo/oshishinobu.html")


@app.route('/en/dojo/info')
def enInfo():
    return render_template("en/dojo/info.html")


@app.route('/en/dojo/calendar')
def enCalendar():
    return render_template("en/dojo/calendar.html")


@app.route('/en/dojo/photoalbum')
def enPhotoalbum():
    return render_template("en/dojo/photoalbum.html")


@app.route('/en/dojo/nieuwsbrief')
def enNieuwsbrief():
    return render_template("en/dojo/nieuwsbrief.pdf")


@app.route('/en/dojo/syllabus')
def enSyllabus():
    return render_template("en/dojo/syllabus.html")


@app.route('/en/kyokushin/geschiedenis')
def enHistory():
    return render_template("en/kyokushin/history.html")


@app.route('/en/kyokushin/spirit')
def enSpirit():
    return render_template("en/kyokushin/spirit.html")


@app.route('/en/kyokushin/warmingup')
def enWarmingup():
    return render_template("en/kyokushin/warmingup.html")


@app.route('/en/kyokushin/kihon')
def enKihon():
    return render_template("en/kyokushin/kihon.html")


@app.route('/en/kyokushin/kata')
def enKata():
    return render_template("en/kyokushin/kata.html")


@app.route('/en/kyokushin/kumite')
def enKumite():
    return render_template("en/kyokushin/kumite.html")


@app.route('/links')
@app.route('/en/links')
def enLinks():
    return render_template("en/links.html")


#--------------------------------------------------------------------

#Geeft de functie voor de Engelstalige pagina weer bij een Nederlandstalige pagina.
@app.context_processor
def returnEnglishPage():
    def englishPage(currenturl, currentrooturl):
        currenturlString = currenturl.encode('ascii', 'ignore')
        currentrooturlString = currentrooturl.encode('ascii', 'ignore')
        if currenturlString == currentrooturlString:
            return "enIndex"
        page = currenturlString.replace(currentrooturlString, "")
        page = page.replace("kyokushin/", "")
        page = page.replace("dojo/", "")
        page = page.replace("nieuws", "news")
        page = page.replace("geschiedenis", "history")
        page = page.replace("opwarming", "warmingup")
        page = page.replace("fotoalbum", "photoalbum")
        page = page.replace("kalender", "calendar")
        page = page.replace("dojobeheer", "dojomanagement")
        page = page.replace("lidtoevoegen", "dojomanagement")
        page = page.replace("lidverwijderen", "dojomanagement")
        page = page.replace("profiel", "profile")
        page = page.replace("instellingen", "settings")
        pageEnglish = page.replace("en/", "")
        pageEnglish = "en" + pageEnglish.replace("nl/", "")
        return pageEnglish[0:2] + pageEnglish[2].upper() + pageEnglish[3:]

    return dict(englishPage=englishPage)


#Geeft de functie voor de overeenkomstige Nederlandstalige pagina weer bij een Engelstalige pagina.
@app.context_processor
def returnDutchPage():
    def dutchPage(currenturl, currentrooturl):
        currenturlString = currenturl.encode('ascii', 'ignore')
        currentrooturlString = currentrooturl.encode('ascii', 'ignore')
        if currenturlString == currentrooturlString:
            return "nlIndex"
        page = currenturlString.replace(currentrooturlString, "")
        page = page.replace("kyokushin/", "")
        page = page.replace("dojo/", "")
        page = page.replace("news", "nieuws")
        page = page.replace("history", "geschiedenis")
        page = page.replace("warmingup", "opwarming")
        page = page.replace("photoalbum", "fotoalbum")
        page = page.replace("calendar", "kalender")
        page = page.replace("dojomanagement", "dojobeheer")
        page = page.replace("lidtoevoegen", "dojobeheer")
        page = page.replace("lidverwijderen", "dojobeheer")
        page = page.replace("profile", "profiel")
        page = page.replace("settings", "instellingen")
        pageDutch = page.replace("nl/", "")
        pageDutch = "nl" + pageDutch.replace("en/", "")
        return pageDutch[0:2] + pageDutch[2].upper() + pageDutch[3:]

    return dict(dutchPage=dutchPage)

#--------------------------------------------------------------------
