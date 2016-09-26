# coding: utf-8
import aiml

ai = aiml.Kernel() # inicialização
ai.learn('std-startup.xml') # lê o arquivo principal da AIML e faz referências aos outros
ai.respond("LOAD AIML B")

def responde_mensagem(mensagem):
	print mensagem
	resposta = ai.respond(mensagem)
	print resposta
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
