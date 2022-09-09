from urllib import response
from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_names',  methods=['GET'])
def get_location_names():

    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():

    body = request.get_json()
    if(body):
        print(body)
        response = jsonify({
            "estimated_price": util.get_estimated_price(body['location'], body['total_sqft'], body['bhk'], body['bath'])
        })
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    else:
        return jsonify({
            "msg": 'Invalid input'
        })


if __name__ == "__main__":
    print('Starting python flask server')
    util.load_saved_artifacts()
    app.run(debug=True)
