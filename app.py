from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import io
from scripts import *

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():

   return jsonify({"message": "Orbit Web Template says: Backend here!"})
   

# Rota para receber o arquivo csv
@app.route("/api/gettiktokdata", methods=['GET', 'POST'])
def gettiktokdata():

   jsonData = request.get_json()

   keyword = jsonData['keyword']
   region = jsonData['region']
   sort = jsonData['sort']
   dataPostagem = jsonData['dataPostagem']
   data_full = search_tiktok(keyword, region, sort, dataPostagem)

   return jsonify(data_full)   


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
