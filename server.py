#coding: utf-8

from flask import Flask, Response, request
import json, random, urllib2
import temp_api
app = Flask(__name__)

piadas = ["MANDA UMA PIADA","CONTE UMA PIADA","PIADAS"]
cantadas = ["MANDE UMA CANTADA","CONTE UMA CANTADA","CANTADAS"]
ditados = ["MANDE UM DITADO","CONTE UM DITADO","DITADOS"]
tempo = "TEMPO EM:"

def salva_frase_arquivo(texto):
	arquivo = open("frases.txt", "r+")
	frases = arquivo.readlines()
	if not texto+"\n" in frases:
		arquivo.write(texto+"\n")
	arquivo.close()

def pesquisa_e_retorna_frase(texto):
	arquivo = open("frases.txt", "r+")
	frases = arquivo.readlines()
	if not texto+"\n" in frases:
		arquivo.write(texto+"\n")
	arquivo.close()
	return random.choice(frases)

def pesquisa_e_retorna_piada():
	arquivo = open("Piadas.txt", "r+")
	frases = arquivo.readlines()
	arquivo.close()
	return random.choice(frases)

def pesquisa_e_retorna_cantadas():
	arquivo = open("Cantadas.txt", "r+")
	frases = arquivo.readlines()
	arquivo.close()
	return random.choice(frases)

def pesquisa_e_retorna_ditados():
	arquivo = open("Ditados.txt", "r+")
	frases = arquivo.readlines()
	arquivo.close()
	return random.choice(frases)

def respondendo_pergunta(texto):
	if texto.find("Você responde perguntas"):
		return "Sim eu sei responder perguntas"
	return "Já já respondo perguntas"

@app.route('/primeiraconexao', methods=['GET'])
def primera_conexao():
	return 'Olá, me chamo Job. É estou aqui para conversar com você.\n' + 'Você pode me pedir: Piadas, Cantadas, Ditados. É so escrever que respondo...😎'

@app.route('/mensagem',methods=['PUT'])
def teste():
	
	try:
		texto = request.data
		texto = str(texto)
		if "Qual seu nome" == texto.strip():
			return "Job"		
		elif  texto.strip().upper() in piadas:
			return pesquisa_e_retorna_piada()
		elif texto.strip().upper() in cantadas:
			return pesquisa_e_retorna_cantadas()
		elif texto.strip().upper() in ditados:
			return pesquisa_e_retorna_ditados()
		elif not texto.strip().upper().find(tempo):
			return temp_api.obtem_temperatura(texto)
		return pesquisa_e_retorna_frase(texto)
	except Exception as e:
		raise e
	
	return 'Ops, houve um erro no servidor. Em breve estaremos funcionando novamente.'

def run(host='0.0.0.0',port=8080,debug=False):
	app.debug = debug
	app.run(host=host, port=port)

if __name__ == '__main__':	
	import sys
	reload(sys)  
	sys.setdefaultencoding('utf-8')
	run(debug='-d' in sys.argv or '--debug' in sys.argv)
