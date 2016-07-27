#coding: utf-8

import json, urllib2

tempo = "TEMPO EM:"
tempo_split = 'TEMPO EM:'

API = 'http://api.openweathermap.org/data/2.5/weather?q={0}&units=metric&appid=5149f44d6754809fbf37e21d8afc9b4a'

def obtem_temperatura(cidade):
	cdd = ((cidade.upper()).replace(tempo,"")).strip()
	try:
		city = cdd.replace(" ","%20")
		retorno = urllib2.urlopen(API.format(city)).read()
		dados = json.loads(retorno)
		temp = dados['main']['temp']
		resposta = 'A Temperatura da cidade de ' + cdd + ' e: ' + str(temp) + "ºc"
		return resposta
	except:
		return 'Não foi possivel obter a temperatura da cidade.'
