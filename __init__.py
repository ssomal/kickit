from flask import Flask, request, jsonify, make_response, render_template, session
from flask_cors import CORS
import logging
import config
import kickit

app = Flask(__name__)
CORS(app)

file_handler = logging.FileHandler(filename='/tmp/kickit_error.log')
file_handler.setLevel(logging.WARNING)
app.logger.addHandler(file_handler)

PREFIX = "/kickit"

@app.route(PREFIX + '/sessionstart', methods = ['POST'])
def sessionStart():
    pObj = request.data
    rObj = wondor.createSession(pObj)
    return jsonify(rObj)


@app.route(PREFIX + '/isvalidsession/<sessionid>', methods = ['POST'])
def checkValid():
    pObj = request.data
    rObj = wondor.checkValidity(pObj)
    return jsonify(rObj)

@app.route(PREFIX + '/addmember/<sessionid>', methods = ['POST'])
def addMember():
    pObj = request.data
    rObj = wondor.addMemberToSession(pObj)
    return jsonify(rObj)

@app.route(PREFIX + '/addactivity/<sessionid>', methods = ['POST'])
def addActivity():
    pObj = request.data
    rObj = wondor.addActivityToSession(pObj)
    return jsonify(rObj)

@app.route(PREFIX + '/removeactivity/<sessionid>', methods = ['POST'])
def removeActivity():
    pObj = request.data
    rObj = wondor.removeActivityFromSession(pObj)
    return jsonify(rObj)

@app.route(PREFIX + '/activitylist/<sessionid>')
def getActivity():
    if sessionid:
        rObj = wondor.getActivityList(sessionid)
    else:
        rObj =  {'error':1,'desc':'No Session Id Provided'}


@app.route(PREFIX + '/getresult/<sessionid>')
def getResult():
    if sessionid:
        rObj = wondor.getMatchResults(sessionid)
    else:
        rObj = {'error':1,'desc':'No Session Id Provided'}


if __name__ == '__main__':
   app.run(debug = True)
