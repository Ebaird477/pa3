#usr/bin/python3
import json
from flask import Flask, request, jsonify

app = Flask (__name__)
global setTemp
global temp

temp = 85
setTemp = 86

@app.route('/ThermsAreUs/api/v1.0/current-temp', methods=['GET'])
def get_current():
    return jsonify({'current temperature': temp})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['GET'])
def get_setpoint():
    return jsonify({'temperature to set': setTemp})

@app.route('/ThermsAreUs/api/v1.0/current-setpoint', methods=['PUT'])
def put_setpoint():
    global setTemp
    #print(request.data)
    #print(json.loads(request.data)['x'])
    setTemp = json.loads(request.data)['setTemp']
    return jsonify({'temperature to set': setTemp})

if __name__ == '__main__':
        app.run(debug=True)