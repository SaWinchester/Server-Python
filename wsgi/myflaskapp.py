#coding: utf-8

from flask import Flask, Response, request
from jobaiml import *
import json, temp_api
import sys
app = Flask(__name__)

tempo = "TEMPO EM:"

'''Obtem a primeira conexão com o servidor e retorna mensagem padrão do Aplicativo'''
@app.route('/', methods=['GET'])
def index():
	return "App de Conversa chamado JOB, foi desenvolvido com base no AIML..."

@app.route('/primeiraconexao', methods=['GET'])
def primera_conexao():
	id_conexao_job = gera_id_job()
	print id_conexao_job
	return json.dumps({"mensagem":u"Olá, me chamo Job. É estou aqui para conversar com você. Você pode me pedir: Piadas, Cantadas, Ditados. É so escrever que respondo...😎"})

@app.route('/mensagem',methods=['PUT'])
def mensagem():
	
	try:
		jsonData = json.loads(request.data)
		texto = jsonData['mensagem']
		print texto
		if not texto.strip().upper().find(tempo):
			return json.dumps({"mensagem":temp_api.obtem_temperatura(texto)})
		return json.dumps({"mensagem":responde_mensagem(texto)})
	except Exception as e:
		raise e
	
	return json.dumps({'mensagem':u'Ops, houve um erro no servidor. Em breve estaremos funcionando novamente.'})

if __name__ == "__main__":
	reload(sys)  
	sys.setdefaultencoding('utf-8')
	inicializa_aiml()
	app.run()
