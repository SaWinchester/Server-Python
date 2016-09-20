# coding: utf-8
import aiml
#ai = aiml.Kernel() # inicialização
#ai.learn('*.aiml') # lê o arquivo principal da AIML e faz referências aos outros
#ai.respond('s') # faz com que os outros arquivos da AIML sejam carregados

def responde_mensagem(mensagem):
	ai = aiml.Kernel() # inicialização
	ai.learn('*.aiml') # lê o arquivo principal da AIML e faz referências aos outros
	print mensagem
	resposta = ai.respond(mensagem)
	print resposta
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
