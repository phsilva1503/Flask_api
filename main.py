from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id):
	return jsonify({'id':id, 'nome':'Pedro', 'profissao':'desenvolvedor'})

@app.route('/soma/<:valor1>/<int:valor2>/')
def soma (valor1,valor2):
	return jsonify ({'soma': valor1 + valor2 })



if __name__=='__main__':
	app.run(host='0.0.0.0', port=81, debug = True)