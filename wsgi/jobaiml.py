# coding: utf-8
import aiml
import os

os.chdir('app-root/data/')

ai = aiml.Kernel() # inicialização
ai.learn('*') # lê o arquivo principal da AIML e faz referências aos outros

def responde_mensagem(mensagem):
	print mensagem
	resposta = ai.respond(mensagem)
	print resposta
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
