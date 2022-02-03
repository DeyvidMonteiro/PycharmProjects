from flask import Flask, jsonify, request

app = Flask = Flask(__name__)


@app.route('/<int:id>')
def pessoa(id):
    soma = 1 + int(id)
    return jsonify({'id': id, 'nome': 'Deyvid'})


@app.route('/soma/<int:valor1>/<int:valor2>/')
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})


@app.route('/soma/', methods=['POST'])
def soma():
    dados = request.data
    print(dados)
    return 'soma'



if __name__ == '__main__':
    app.run(debug=True)
