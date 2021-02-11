import flask

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

@app.route('/log/chargestorm/notify', methods=['GET']) 
def get_notify():
    return flask.jsonify({'notification':notifications})

@app.route('/log/chargestorm/notify', methods=['POST'])
def post_notify():
    msg = flask.request.get_json()
    msgType = msg["messageType"]
    if(msgType == "transactionStart"):
        print("Respond to start")
        return flask.jsonify({"accepted":True,"errorCode":"NO_Error"}),200
    elif(msgType == "transactionStop"):
        print("Respond to stop")
        return flask.jsonify({"accepted":True,"errorCode":"NO_Error"}),200
    else:
        return flask.jsonify({"accepted":False, "error_code":"Wrong_MessageType"}),400
    return 

if __name__ == '__main__':
    app.run(debug=False)