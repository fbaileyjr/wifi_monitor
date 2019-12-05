#! /usr/bin/python -tt

#from surveyWifi import *
import time, ConfigParser
#from newtestwifi import *
#from testwifi import *
import subprocess
from subprocess import *
from postStatusData import *
import uuid

cmd1="ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def get_ip_address(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
        )[20:24])


me = postCheckinData()
ipaddr = run_cmd(cmd1)
while ipaddr == '':
        ipaddr = run_cmd(cmd1)

doCheckIn = me.doPost(ipaddr.strip(), run_cmd('hostname'),'2')
