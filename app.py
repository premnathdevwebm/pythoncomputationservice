import json
from flask import Flask, request
from FirstYearPhysics import FirstYPhysics
from physics_acet import PHY_acet
from Chemistry_acet import Chem_acet
app = Flask(__name__)
#app.debug = False

@app.route('/<param1>', methods=['POST'])
def hello_world(param1):
    data = request.json
    if data is None:
        return 'Missing data in the request body', 400
    argument_list = data.get('argument')
    try:
        if(param1 == "Vibrational_magnetometer_acet"):
           return PHY_acet(argument_list).VB_Mag()
    except ValueError:
                return(json.dumps({"error":"value added error"}))

if __name__ == '__main__':
    app.run()

