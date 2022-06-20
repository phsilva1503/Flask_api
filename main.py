from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<id>')
def pessoa(id):
	return jsonify({'id':id, 'nome':'Pedro', 'profissao':'desenvolvedor'})



if __name__=='__main__':
	app.run(host='0.0.0.0', port=81, debug = True)