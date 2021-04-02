import requests
import json

#Christians API-key till rebase
api_key = 'ka8HR1KQMGi5WySvGyATV3PprcZeZafABl3Ms6AH2vw'


#'87893bbd-1b9a-49fb-88b6-32968f060552' är den test-site som är gjord för HSB-LL
url = 'https://api.rebase.energy/platform/v1/site/latest_forecast/87893bbd-1b9a-49fb-88b6-32968f060552'

headers = {
  'GL-API-KEY': api_key
}

params = {
  'type': 'prioritized',      #'ai', 'prioritized', 'physical'
}


#forecasten returneras på en kvartsbasis
def get_solar_forecast(start_time):


  st = round_to_quarter(start_time)
  #index = hour * 4 + minute / 5
  index = int(int(st[0:2])*4 + int(st[3:5])/5) 
  response = requests.get(url, headers=headers, params=params)

  result = response.json()
  est_solar = {}
  for i in range(96):                       #get all values for the next 24 hours
    est_solar[result['valid_time'][index+i][11:16]] = round(result['forecast'][index+i],2)

  return est_solar


def round_to_quarter(start_time):
  minute = int(start_time[3:5])
  if(minute < 15):
    return start_time[0:3] + '00'
  if(minute < 30):
    return start_time[0:3] + '15'
  if(minute < 45):
    return start_time[0:3] + '30' 
  if(minute < 60):
    return start_time[0:3] + '45'       
