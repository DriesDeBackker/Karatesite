import calendar
from datetime import *
from flask_app import app

#-------------------------------------------------

#Haal het huidige jaar op.
def getCurrentYear():
        return datetime.now().year

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnCurrentYear():
    return dict(getCurrentYear = getCurrentYear)

#-------------------------------------------------

#Haal de huidige maand op.
def getCurrentMonth():
    return datetime.now().month

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnCurrentMonth():
    return dict(getCurrentMonth = getCurrentMonth)

#-------------------------------------------------

#Haal de Nederlandse naam van de huidige maand op.
def getCurrentMonthNameNL():
    maanden = ('januari', 'februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december')
    return maanden[datetime.now().month - 1]

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnCurrentMonthNameNL():
    return dict(getCurrentMonthNameNL = getCurrentMonthNameNL)

#-------------------------------------------------

#Haal de Nederlandse naam van de volgende maand op.
def getNextMonthNameNL():
    return getRelativeMonthNameNL(1)

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnNextMonthNameNL():
    return dict(getNextMonthNameNL = getNextMonthNameNL)

#-------------------------------------------------

#Haal de Nederlandse naam van een maand relatief t.o.v. de huidige maand op.
def getRelativeMonthNameNL(offset):
    maand = getRelativeYearAndMonth(offset)[1]
    maanden = ('januari', 'februari','maart','april','mei','juni','juli','augustus','september','oktober','november','december')
    return maanden[maand - 1]

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnRelativeMonthNameNL():
    return dict(getRelativeMonthNameNL = getRelativeMonthNameNL)

#-------------------------------------------------

#Haal het huidige jaar en de huidige maand op.
def getCurrentYearAndMonth():
    return [getCurrentYear(),getCurrentMonth()]

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnCurrentYearAndMonth():
    return dict(getCurrentYearAndMonth = getCurrentYearAndMonth)

#-------------------------------------------------

#Bereken het jaar en de maand vertrekkend van dit jaar en deze maand via een offset in aantal maanden.
def getRelativeYearAndMonth(offset):
        relativeYear = getCurrentYear()
        relativeMonth = getCurrentMonth()
        relativeMonth += offset
        while relativeMonth <= 0:
            relativeMonth += 12
            relativeYear -= 1
        while relativeMonth > 12:
            relativeMonth -= 12
            relativeYear += 1
        return [relativeYear, relativeMonth]

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnRelativeYearAndMonth():
    return dict(getRelativeYearAndMonth = getRelativeYearAndMonth)

#-------------------------------------------------

#Haal een string op van 42 dagen waaronder de dagen van de huidige maand
    #en de dagen errond, nodig voor een complete tabel.
def getDaysOfCurrentMonth():
    return getDaysOfMonth(getCurrentYear(), getCurrentMonth())

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfCurrentMonth():
    return dict(getDaysOfCurrentMonth = getDaysOfCurrentMonth)

#-------------------------------------------------

#Geef een matrix terug van 42 dagen waaronder de dagen van de huidige maand
    #en de dagen errond, nodig voor een complete tabel
    #waarbij de rijen van de matrix de weken aanduiden.
def getDaysOfCurrentMonthMatrix():
    return getDaysOfMonthMatrix(getCurrentYear(), getCurrentMonth())

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfCurrentMonthMatrix():
    return dict(getDaysOfCurrentMonthMatrix = getDaysOfCurrentMonthMatrix)

#-------------------------------------------------

#Haal een string op van 42 dagen waaronder de dagen van de volgende maand
    #en de dagen errond, nodig voor een complete tabel.
def getDaysOfNextMonth():
    nextMonth = getRelativeYearAndMonth(1)[1]
    yearNextMonth = getRelativeYearAndMonth(1)[0]
    return getDaysOfMonth(yearNextMonth, nextMonth)

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfNextMonth():
    return dict(getDaysOfNextMonth = getDaysOfNextMonth)

#-------------------------------------------------

#Geef een matrix terug van 42 dagen waaronder de dagen van de volgende maand
    #en de dagen errond, nodig voor een complete tabel
    #waarbij de rijen van de matrix de weken aanduiden.
def getDaysOfNextMonthMatrix():
    nextMonth = getRelativeYearAndMonth(1)[1]
    yearNextMonth = getRelativeYearAndMonth(1)[0]
    return getDaysOfMonthMatrix(yearNextMonth, nextMonth)

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfNextMonthMatrix():
    return dict(getDaysOfNextMonthMatrix = getDaysOfNextMonthMatrix)

#-------------------------------------------------

#Haal een string op van 42 dagen waaronder de dagen van een maand relatief tot de huidige maand
    #en de dagen errond, nodig voor een complete tabel.
def getDaysOfRelativeMonth(offset):
    relativeYearAndMonth = getRelativeYearAndMonth(offset)
    return getDaysOfMonth(relativeYearAndMonth[0],relativeYearAndMonth[1])

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfRelativeMonth():
    return dict(getDaysOfRelativeMonth = getDaysOfRelativeMonth)

#-------------------------------------------------

#Geef een matrix terug van 42 dagen waaronder de dagen van een maand relatief tot de huidige maand
    #en de dagen errond, nodig voor een complete tabel
    #waarbij de rijen van de matrix de weken aanduiden.
def getDaysOfRelativeMonthMatrix(offset):
    relativeYearAndMonth = getRelativeYearAndMonth(offset)
    return getDaysOfMonthMatrix(relativeYearAndMonth[0],relativeYearAndMonth[1])

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfRelativeMonthMatrix():
    return dict(getDaysOfRelativeMonthMatrix = getDaysOfRelativeMonthMatrix)

#-------------------------------------------------

#Bereken een string van 42 dagen waaronder de dagen van de opgegeven maand in het opgegeven jaar
    #en alle dagen ervoor die nodig zijn om de week te vervolmaken
    # en alle dagen erna die nodig zijn om aan 42 dagen te komen.
def getDaysOfMonth(year,month):
    cal = calendar.Calendar()
    days = []
    #Haal de dagen van deze maand op, plus de dagen errond nodig voor een volledige week, als int waardes
        #en steek ze in een lijst.
    for i in cal.itermonthdates(year,month):
        days.append(i.day)
    #Bereken de volgende (eventueel) toe te voegen datum.
        #Dit is de vorige datum + 1, tenzij de vorige datum de laatste dag van de maand is.
    currentLastDay = days[len(days)-1]
    if currentLastDay > 10:
        currentLastDay = 0
    dayToAdd = currentLastDay + 1
    #Zolang het aantal data niet 42 is, voeg data toe.
    while not len(days) == 42:
        days.append(dayToAdd)
        dayToAdd += 1
    #Zet de int waardes van days om naar str waardes in daysResult
        #waarbij aan getallen van 1 cijfer vooraan een nul wordt toegevoegd.
    daysResult = []
    for i in days:
        day = str(i)
        if len(day) == 1:
            day = '0' + day
        daysResult.append(day)
    return daysResult

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfMonth():
    return dict(getDaysOfMonth = getDaysOfMonth)

#-------------------------------------------------

#Geef een matrix terug van de 42 dagen in getDaysOfMonth(year,month)
    #waarbij elke rij voor een andere week staat.
def getDaysOfMonthMatrix(year,month):
    days = getDaysOfMonth(year,month)
    matrix = []
    for i in range (0,6):
        matrix.append([])
        for j in range(0,7):
            entry = days[i*7+j]
            matrix[i].append(entry)
    return matrix

#Maak bovenstaande functie bereikbaar voor Jinja. 
@app.context_processor
def returnDaysOfMonthMatrix():
    return dict(getDaysOfMonthMatrix = getDaysOfMonthMatrix)

#-------------------------------------------------
        


