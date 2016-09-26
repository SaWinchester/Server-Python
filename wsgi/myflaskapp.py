#coding: utf-8

from flask import Flask, Response, request
from jobaiml import responde_mensagem
import json
import temp_api
app = Flask(__name__)

tempo = "TEMPO EM:"

'''Obtem a primeira conexão com o servidor e retorna mensagem padrão do Aplicativo'''
@app.route('/', methods=['GET'])
def index():
	return "App de Conversa chamado JOB, foi desenvolvido com base no AIML..."

@app.route('/primeiraconexao', methods=['GET'])
def primera_conexao():
	return "Olá, me chamo Job. É estou aqui para conversar com você. Você pode me pedir: Piadas, Cantadas, Ditados. É so escrever que respondo...😎"

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

if __name__ == "__main__":
	app.run()
