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
  response = requests.get(url, headers=headers, params=params)

  result = response.json()
  est_solar = {}
  for x in range(len(result['valid_time'])):    #go through the results
    if(result['valid_time'][x][11:16]== st):    #until we find the "now"-time
      for i in range(96):                       #get all values for the next 24 hours
        est_solar[result['valid_time'][x+i][11:16]] = round(result['forecast'][x+i],2)
      break 

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
