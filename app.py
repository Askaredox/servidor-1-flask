from flask import Flask, request
from flask_cors import CORS
from servicio import Servicio

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origin": "*"}})


@app.route('/')
def check():
    return "Todo good"

@app.route('/api/add', method=['POST'])
def add():
    if request.method == 'POST':
        content = request.get_json()
        autor = content['autor']
        nota = content['nota']
        return Servicio.send_data(autor, nota)
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
