# coding: utf-8
import aiml

ai = aiml.Kernel() # inicialização
ai.learn('$OPENSHIFT_DATA_DIR/*') # lê o arquivo principal da AIML e faz referências aos outros

def responde_mensagem(mensagem):
	print mensagem
	resposta = ai.respond(mensagem)
	print resposta
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
