import flask
import pymongo

# This flask REST-api serves the purpose of answering the notify start and notify stop
# requests sent by Chargestorm to confirm starting and stopping the charging
# the transactionID and the tagID are stored on a database
# to enable the microcontroller to receive the tagID to use
client = pymongo.MongoClient("mongodb+srv://samjons:q7Jn863R2TWvj9K2@kandidat.gcnnv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.information
coll = db.chargestorm
app = flask.Flask(__name__)

notifications = [
    {
        "messageType":"transactionStart",
        "evseID": "number",
        "tagID": "tagid",
        "timeStamp": "date",
        "sessionId": "sessionId",
        "transactionId": "transactionId"
    },
    {
        "messageType":"transactionStop",
        "evseId":"number",
        "kWh":"kWh",
        "timeStamp":"date",
        "sessionId":"sessionId",
        "transactionId":"transactionId"
    }
]
@app.route('/', methods=['GET'])
def home():
    return "Hello World!"

#For the microcontroller to send a GET request to the specified URL and receive the RFID tag information
@app.route('/log/chargestorm/notify', methods=['GET']) 
def get_notify():
    msg = flask.request.get_json()
    transactionIDmsg = msg["transactionID"]
    rfid = coll.find_one({"_id":transactionIDmsg})
    return(flask.jsonify(rfid))

#Endpoint for chargestorm to send the notifyStart and notifyStop requests
@app.route('/log/chargestorm/notify', methods=['POST'])
def post_notify():
    #The json message sent by chargestorm
    msg = flask.request.get_json()
    #msgType gets set to either transactionStart or transactionStop depending on which one chargestorm sent
    msgType = msg["messageType"]
    #the RFID tag ID is set depending on what chargestorm sent
    rfid = msg["tagID"]
    #the transactionID is used as an identifier for indexing in the database
    transactionIDmsg = msg["transactionID"]
    key = {
        "_id":transactionIDmsg
    }
    data = {
        "$set":{
            "_id": transactionIDmsg,
            "rfid": rfid
        }
    }
    if(msgType == "transactionStart"):
        print("Respond to start")
        #if an entry with the same transactionID is already stored in the database, then update that entry
        #else create a new entry in the database with that transactionID
        coll.update_one(key, data, upsert = True)
        return flask.jsonify({"accepted":True,"errorCode":"NO_Error"}),200
    elif(msgType == "transactionStop"):
        print("Respond to stop")
        return flask.jsonify({"accepted":True,"errorCode":"NO_Error"}),200
    else:
        return flask.jsonify({"accepted":False, "error_code":"Wrong_MessageType"}),400
    return 

if __name__ == '__main__':
    app.run(host = "127.0.0.1", port = 5001)