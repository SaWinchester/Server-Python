#coding: utf-8

import os, sys
from server import app as application, run

if __name__ == '__main__':

	ip = '0.0.0.0'
	port = int(80)

    # Para detalhae melhor os Logs no OpenShift
	application.config['PROPAGATE_EXCEPTIONS'] = True
	reload(sys)  
	sys.setdefaultencoding('utf-8')

	run(ip, port,True)
