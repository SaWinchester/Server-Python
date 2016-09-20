#coding: utf-8

import os, sys
from server import app as application, run

if __name__ == '__main__':

	ip = os.environ.get('OPENSHIFT_PYTHON_IP', '192.168.0.104')
	port = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 60026))

    # Para detalhae melhor os Logs no OpenShift
	application.config['PROPAGATE_EXCEPTIONS'] = True
	reload(sys)  
	sys.setdefaultencoding('utf-8')

	run(ip, port,True)
