import datetime
#TODO ta fram dictionary och slå samman alla parametrar för angiven tid
#TODO fråga living lab om PV data för att jämföra med väder data
#TODO uppdatera hur mycket batteriet har laddats?
priser = {
    0: 67,
    1: 65,
    2: 50,
    3: 45,
    4: 46,
    5: 45,
    6: 58,
    7: 68,
    8: 44,
    9: 67,  # Dessa ska beräknas senare
    10: 80,
    11: 43,
    12: 50,
    13: 86,
    14: 79,
    15: 30,
    16: 87,
    17: 86,
    18: 95,
    19: 87,
    20: 85,
    21: 78,
    22: 74,
    23: 72,
}
def param(time_now,end_time):
    #Om end_time - time_now är större än 12h skickar vi 12 värden tillbaka
    #Om end_time - time_now är mindre än 12h skickar vi återstående värden tillbaka
    params ={

    }
    i = int((((end_time-time_now).total_seconds())/3600)+0.5)   #laddningstid avrundat till timmar
    #print(i)
    #print("antal timmar avrundat")
    y = int((time_now+datetime.timedelta(minutes = 30)).strftime("%H"))

    #print(y)
    #print("vilken timme som är nu")
    if i < 12:
        for j in range(y,y+i+1):
            #print(j)
            p = j % 24
            params[p] = priser[p]
    else:
        i = 12
        for j in range(y,y+i+1):
            p = j % 24
            params[p] = priser[p]
    #print(params)
    #print("retur från params")
    return params

#end_time = datetime.datetime(2021,3,3,8,0,0)
#param(datetime.datetime.now(),end_time)
#print(param(datetime.datetime.now(),end_time))


