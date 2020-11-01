# Api rest creada con flask que realiza la conversión de fechas de 
# formato '2020-11-29' a timestamp.

from flask import Flask, render_template, make_response, jsonify, request
from service.converter_date import converter

app = Flask(__name__)

PORT = 2560
HOST = '0.0.0.0'


# Inicio de la api
@app.route("/", methods=['GET'])
def home():
    if request.args:
        date = request.args
        if 'date' in date:
            res = converter(date['date'])
            res = make_response(jsonify(res), 200)
            return res
        res = make_response(jsonify({"error": "La key debe llamarse 'date'."}), 400)
        return res 

    res = make_response(jsonify({"error": "No se envio ninguna fecha."}), 400)
    return res        


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=True)