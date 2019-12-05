#! /usr/bin/python -tt

#from surveyWifi import *
import time, ConfigParser
#from testfreewifi import *
#from newtestwifi import *
#from testwifi import *
from testwifiperf import *
import subprocess
from subprocess import *
from postStatusData import *
import uuid

config = ConfigParser.RawConfigParser()
config.read('/usr/share/drone/wifidrone/wifidrone.conf')
test1 = config.get("RUNTESTS", "1")
test2 = config.get("RUNTESTS", "2")
test3 = config.get("RUNTESTS", "3")
test4 = config.get("RUNTESTS", "4")
test5 = config.get("RUNTESTS", "5")
test6 = config.get("RUNTESTS", "6")
run = 1
netnormal = "/usr/share/drone/scripts/networknormal.sh"
cleanup = "sudo pkill dhclient"

print test1
print test2
print test3
print test4
print test5
print test6


def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        time.sleep(5)
        return output

def kill_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]

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
		doWifiPerfTest(test1,myguid)
		time.sleep(10)
		doWifiPerfTest(test3, myguid)
		time.sleep(10)
		#doWifiPerfTest(test2, myguid)
		#doWifiPerfTest(test4, myguid)
		doWifiPerfTest(test5, myguid)
		time.sleep(10)
		doWifiPerfTest(test6, myguid)
		print 'Sleeping'
		doCheckIn = me.doPost(get_ip_address('eth0'), run_cmd('hostname'),'0')
		kill_cmd(cleanup)
		#time.sleep(900)
		run = 0
	except Exception as err:
		print str(err)
		run_cmd(netnormal)
	except KeyboardInterrupt:
		run_cmd(netnormal)

print 'Stopped'



