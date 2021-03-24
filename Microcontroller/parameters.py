import datetime
#TODO ta fram dictionary och slå samman alla parametrar för angiven tid
#TODO fråga living lab om PV data för att jämföra med väder data
#TODO uppdatera hur mycket batteriet har laddats?
# #Nyckel = datum + H, värde = pris/load/sol Gör 3 separata till att börja med
year = 2021
mon = 1
day = 1
hou = 0
tidspris = {
}
date = datetime.datetime(year, mon, day, hou)
for j in range(365 * 24 + 1):
    #print (date)
    tidspris[date] =  25                                #Skapar en dictionary med alla datum/timslag som nycklar för år 2021
    date = date + datetime.timedelta(hours=1)
                                                        #Värden kan dock uppdateras varje gång om man tänker forecast
def param(time_now,end_time):
    #Om end_time - time_now är större än 12h skickar vi 12 värden tillbaka
    #Om end_time - time_now är mindre än 12h skickar vi återstående värden tillbaka
    params ={

    }
    i = int((((end_time-time_now).total_seconds())/3600)+0.5)   #laddningstid avrundat till timmar
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
    if i < 24:
        for j in range(y,y+i+1):
            #print(j)
           #print(p)
            params[p] = tidspris[p]
            p = p + datetime.timedelta(hours=1)
    else:
        i = 24
        for j in range(y,y+i+1):
            #print(p)
            params[p] = tidspris[p]
            p = p + datetime.timedelta(hours=1)
    print(params)

    return params

#end_time = datetime.datetime(2021,3,27,8,0,0)
#param(datetime.datetime.now(),end_time)
#print(param(datetime.datetime.now(),end_time))


#forecastpv - producerar 1kwh 2kwh 5kwh - använda alla dem
#sen kolla på load typ, bara living lab, eller hela sverige? - Historisk data -- Genomsnitt
