import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask rodando no Render!"

@app.route('/dados', methods=['POST'])
def receber_dados():
    dados = request.json
    print("Dados recebidos:", dados)
    return jsonify({"status": "sucesso", "dados": dados}), 200

if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)
