import datetime
#TODO ta fram dictionary och slå samman alla parametrar för angiven tid
#TODO fråga living lab om PV data för att jämföra med väder data
#TODO uppdatera hur mycket batteriet har laddats?
# #Nyckel = datum + H, värde = pris/load/sol Gör 3 separata till att börja med

def get_prices():
    tidspris = {}
    year = 2021
    mon = 1
    day = 1
    hou = 0
    hourprice = [
        16.78,
        16.93,
        17.69,
        19.41,
        21.26,
        22.56,
        40.73,
        43.06,
        44.33,
        43.29,
        43.82,
        41.57,
        40.75,
        40.48,
        40.05,
        40.53,
        40.52,
        41.44,
        42.04,
        41.76,
        36.65,
        26.36,
        23.18,
        22.73
    ]

    wkndprice = [
        22.05,
        20.77,
        20.06,
        20.09,
        21.02,
        22.95,
        22.48,
        22.91,
        24.07,
        29.61,
        27.52,
        24.64,
        23.7,
        22.91,
        21.79,
        21.3,
        20.94,
        24.08,
        37.68,
        29.44,
        23.69,
        21.99,
        18.04,
        16.36
    ]
    date = datetime.datetime(year, mon, day, hou)
    for j in range(365 * 24 + 1):
        #print (j)
        if date.weekday() in [5,6]:
            tidspris[date] =  wkndprice[date.hour]                               #Skapar en dictionary med alla datum/timslag som nycklar för år 2021
        else:
            tidspris[date] =  hourprice[date.hour]                               #Skapar en dictionary med alla datum/timslag som nycklar för år 2021
        date = date + datetime.timedelta(hours=1)
        #print(date.weekday())
    return tidspris                                          #Värden kan dock uppdateras varje gång om man tänker forecast


def param(time_now,end_time):
    #Om end_time - time_now är större än 12h skickar vi 12 värden tillbaka
    #Om end_time - time_now är mindre än 12h skickar vi återstående värden tillbaka
    tidspris = get_prices()
    params ={}
    timmar = int((((end_time-time_now).total_seconds())/3600)+0.5)   #laddningstid avrundat till timmar
    #print(i)
    #print("antal timmar avrundat")
    z = int((time_now+datetime.timedelta(minutes = 0)).strftime("%H"))
    y = int((time_now+datetime.timedelta(minutes = 30)).strftime("%H")) #TODO: Kolla efter buggar vid 23:30 tider

    #print(y)
    #print("vilken timme som är nu")
    if z == 23 and y == 0:
        p = datetime.datetime(time_now.year, time_now.month, time_now.day + 1, y)
    else:
        p = datetime.datetime(time_now.year, time_now.month, time_now.day, y)
    if timmar < 24:
        for j in range(y,y+timmar+1):
            #print(j)
           #print(p)
            params[p] = tidspris[p]
            p = p + datetime.timedelta(hours=1)
    else:
        timmar = 24
        for j in range(y, y+timmar+1):
            #print(p)
            params[p] = tidspris[p]
            p = p + datetime.timedelta(hours=1)
    #print(params)

    return params

end_time = datetime.datetime(2021,3,27,8,0,0)
param(datetime.datetime.now(),end_time)
print(param(datetime.datetime.now(),end_time))


#forecastpv - producerar 1kwh 2kwh 5kwh - använda alla dem
#sen kolla på load typ, bara living lab, eller hela sverige? - Historisk data -- Genomsnitt
