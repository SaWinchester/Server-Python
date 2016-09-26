# coding: utf-8
import aiml
import os

ai = aiml.Kernel() # inicialização

if os.path.isfile("bot_brain.brn"):
    ai.bootstrap(brainFile = "bot_brain.brn")
else:
    ai.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML Bb")
    ai.saveBrain("bot_brain.brn")

def responde_mensagem(mensagem):
	print mensagem
	resposta = ai.respond(mensagem)
	print resposta
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta
