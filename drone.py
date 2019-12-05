#! /usr/bin/python -tt

from surveyWifi import *
import time, ConfigParser
#from testfreewifi import *
from newtestwifi import *
from testwifi import *
import subprocess
from subprocess import *
from postStatusData import *
import uuid

config = ConfigParser.RawConfigParser()
config.read('/usr/share/drone/drone.conf')
test1 = config.get("RUNTESTS", "1")
test2 = config.get("RUNTESTS", "2")
test3 = config.get("RUNTESTS", "3")
test4 = config.get("RUNTESTS", "4")
run = 1
netnormal = "/usr/share/drone/scripts/networknormal.sh"

print test1
print test2
print test3
print test4

#doTest()
def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	time.sleep(5)
	return output

def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,  # SIOCGIFADDR
		struct.pack('256s', ifname[:15])
	)[20:24])

while run == 1:
    try:
        guid = uuid.uuid4()
        myguid = str(guid)
        me = postCheckinData()
        doCheckIn = me.doPost(get_ip_address('eth0'), run_cmd('hostname'),'1')
	#print doCheckIn
	#doSurvey()
        print '>>>>>'
        doWifiTest(test1,myguid)
        doWifiTest(test3, myguid)
	#doWifiTest(test2, myguid)
	doWifiTest(test4, myguid)
        print 'Sleeping'
	doCheckIn = me.doPost(get_ip_address('eth0'), run_cmd('hostname'),'0')
        #time.sleep(900)
	run = 0
    except Exception as err:
		print str(err)
		run_cmd(netnormal)
    except KeyboardInterrupt:
		run_cmd(netnormal)

print 'Stopped'


