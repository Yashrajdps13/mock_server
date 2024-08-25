# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")

@app.route('/')
def home():
    return jsonify({'message': 'Hello World'})

@app.route('/getRoute', methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    data_model = [[17.686815, 83.218483], [11.6234, 92.7265]]
    return jsonify({"Path": data_model})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)