import requests
import json

#Christians API-key till rebase
api_key = 'ka8HR1KQMGi5WySvGyATV3PprcZeZafABl3Ms6AH2vw'


#'87893bbd-1b9a-49fb-88b6-32968f060552' är den test-site som är gjord för HSB-LL
solar_url = 'https://api.rebase.energy/platform/v1/site/forecast/latest/dbcb7636-696d-4279-a5c1-131509e28956'
load_url = 'https://api.rebase.energy/platform/v1/site/forecast/latest/612d5834-0056-482d-b0d3-7a53aa770193'
headers = {
  'GL-API-KEY': api_key
}

params = {
  'type': 'ai',      #'ai', 'prioritized', 'physical'
}


#forecasten returneras på en kvartsbasis
def get_solar_forecast(start_time):


  st = round_to_quarter(start_time)
  #index = hour * 4 + minute / 5
  index = int(int(st[0:2])*4 + int(st[3:5])/15)
  response = requests.get(solar_url, headers=headers, params=params)

  result = response.json()
  est_solar = {}
  solar_forecast = []
  for i in range(96):                       #get all values for the next 24 hours
    est_solar[result['valid_time'][index+i][11:16]] = round(result['forecast'][index+i],2)
    solar_forecast.append(round((result['forecast'][index+i]/0.4),2))
  return solar_forecast



def get_load_forecast(start_time):

  st = round_to_hour(start_time)
  index = int(st[0:2])
  response = requests.get(load_url, headers=headers, params=params)

  result = response.json()
  est = {}
  load_forecast = []
  for i in range(24):                       #get all values for the next 24 hours
    est[result['valid_time'][index+i][11:16]] = round(result['forecast'][index+i],2)
    load_forecast.append(round((result['forecast'][index+i]),2))
  return load_forecast



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

def round_to_hour(start_time):
  hour = int(start_time[0:2])
  minute = int(start_time[3:5])
  if(minute < 30):
    return str(hour) + ':00'
  if(minute < 60):
    return str(hour + 1) + ':00'

#print(get_load_forecast("15:45"))
#print(get_solar_forecast("15:45"))