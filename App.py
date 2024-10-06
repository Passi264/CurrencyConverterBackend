from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)
api_key = os.getenv('EXCHANGE_RATE_API_KEY')

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return "Welcome to the Currency Converter API!"

    elif request.method == "POST":
        data = request.get_json()
        source_currency = data["queryResult"]["parameters"]["unit-currency"]["currency"]
        amount = data["queryResult"]["parameters"]["unit-currency"]["amount"]
        target_currency = data["queryResult"]["parameters"]["currency-name"]
        cf = fetch_conversion_factor(source_currency, target_currency)
        final_amount = amount * cf
        final_amount = round(final_amount, 2)
        response = {
            "fulfillmentText": "{} {} is {} {}".format(amount, source_currency, final_amount, target_currency)
        }
        return jsonify(response)

def fetch_conversion_factor(source, target):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source}/{target}"
    response = requests.get(url)
    respond = response.json()
    return respond["conversion_rate"]

# Handle missing favicon.ico to avoid 404 errors
@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)








# from flask import Flask, request, jsonify
# import requests
#
# app= Flask(__name__)
#
# @app.route('/', methods=["POST"])
# def index():
#     data= request.get_json()
#     source_currency = data["queryResult"]["parameters"]["unit-currency"]["currency"]
#     amount= data["queryResult"]["parameters"]["unit-currency"]["amount"]
#     target_currency= data["queryResult"]["parameters"]["currency-name"]
#     cf = fetch_conversion_factor(source_currency, target_currency)
#     final_amount= amount * cf
#     final_amount=round(final_amount,2)
#     response = {
#         "fulfillmentText": "{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
#     }
#     return jsonify(response)
#
# def fetch_conversion_factor(source,target):
#     url="https://v6.exchangerate-api.com/v6/0277123468f5b1bbe1ad35eb/pair/{}/{}".format(source,target)
#     response= requests.get(url)
#     respond = response.json()
#     return respond["conversion_rate"]
#
# if __name__ == "__main__":
#     app.run(debug=True)




