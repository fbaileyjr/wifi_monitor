#! /usr/bin/python

from subprocess import *
import time
from ssidParse import *

cmd1 = "/usr/share/drone/scripts/iwlistcommands.sh"

def doSurvey():
	
	def run_cmd(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		return output
	
	#iters = 0
	#while iters <= 1:
	#iters = iters + 1
	SSIDLIST = run_cmd(cmd1)
	doSSIDParse(SSIDLIST)
	