########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Accept-Encoding': '',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
    'Authorization': '{access token}',
}

params = urllib.urlencode({
    # Request parameters
    'deliveryarea': '{string}',
    'startTime': '{string}',
    'endTime': '{string}',
})

try:
    conn = httplib.HTTPSConnection('marketdata-api.nordpoolgroup.com')
    conn.request("GET", "/operatingdata/hydroReservoir/content?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Accept-Encoding': '',
    'Ocp-Apim-Subscription-Key': '{subscription key}',
    'Authorization': '{access token}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'deliveryarea': '{string}',
    'startTime': '{string}',
    'endTime': '{string}',
})

try:
    conn = http.client.HTTPSConnection('marketdata-api.nordpoolgroup.com')
    conn.request("GET", "/operatingdata/hydroReservoir/content?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################