#coding: utf-8

from flask import Flask, Response, request
#from jobaiml import responde_mensagem
#import json
#import temp_api
app = Flask(__name__)

tempo = "TEMPO EM:"

'''Obtem a primeira conexão com o servidor e retorna mensagem padrão do Aplicativo'''
@app.route('/', methods=['GET'])
def primera_conexao():
	return "responde_mensagem('Conectar')"

'''@app.route('/primeiraconexao', methods=['GET'])
def primera_conexao():
	return responde_mensagem('Conectar')

@app.route('/mensagem',methods=['PUT'])
def teste():
	
	try:
		texto = request.data
		texto = str(texto)
		if not texto.strip().upper().find(tempo):
			return temp_api.obtem_temperatura(texto)
		return responde_mensagem(texto)
	except Exception as e:
		raise e
	
	return 'Ops, houve um erro no servidor. Em breve estaremos funcionando novamente.'
'''
def run(host='0.0.0.0',port=80,debug=False):
	app.debug = debug
	app.run(host=host, port=port)

if __name__ == '__main__':	
	import sys
	reload(sys)  
	sys.setdefaultencoding('utf-8')
	run(debug='-d' in sys.argv or '--debug' in sys.argv)
