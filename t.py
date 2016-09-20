# coding: utf-8
import aiml
ai = aiml.Kernel() # inicialização
ai.learn('std-startup.xml') # lê o arquivo principal da AIML e faz referências aos outros
ai.respond('load aiml b') # faz com que os outros arquivos da AIML sejam carregados

def responde_mensagem(mensagem):
	resposta = ai.respond(mensagem)
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
