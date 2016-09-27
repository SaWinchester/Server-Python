# coding: utf-8
import aiml
import os
import random

os.chdir('app-root/data/')
#os.chdir('static/')

ai = aiml.Kernel() # inicialização

def inicializa_aiml():
	if os.path.isfile("bot_brain.brn"):
		ai.bootstrap(brainFile = "bot_brain.brn")
	else:
		ai.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
		ai.saveBrain("bot_brain.brn")

def responde_mensagem(mensagem):
	resposta = ai.respond(mensagem)
	if resposta == '':
		return "Eu realmente não compreendo"
	else:
		return resposta

def gera_id_job():
	sessionId = int(random.randint(1,100000000000))
	return sessionId
