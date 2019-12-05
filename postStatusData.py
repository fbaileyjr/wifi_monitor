#!/usr/bin/python -tt

import urllib
import urllib2
import wddx
import subprocess
from subprocess import *

import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/usr/share/drone/drone.conf')
myurl = config.get("PARMS", "POSTURL")
url=myurl
callmethod="dronestatus"
loc = config.get("PARMS", 'LOCATION')
cmd="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"
def run_cmd(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		return output

dronedata = run_cmd(cmd)

class postCheckinData:

    def __init__(self):


        self.droneid = dronedata.strip(' ')
        self.location = loc.strip(' ')

    def doPost(self, ipdata, hostnamedata, rstate):
        self.ipaddr = ipdata
        self.hostname = hostnamedata
	self.rstate = rstate
        try:
                        params = urllib.urlencode({
                                'method': callmethod,
                                'droneid': self.droneid,
                                'location': self.location,
                                'ipaddr': self.ipaddr,
                                'hostname': self.hostname,
				'runstate': self.rstate
                                })
                        response = urllib2.urlopen(url, params).read()
                        return response
                        print response
        except Exception as err:
            return 0
            pass
