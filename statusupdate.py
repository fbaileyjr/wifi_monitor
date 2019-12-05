#!/usr/bin/python -tt

from subprocess import *
from time import sleep, strftime
import ConfigParser
from datetime import datetime
from postStatusData import postData

config = ConfigParser.RawConfigParser()
config.read('/usr/share/drone/drone.conf')
loc = config.get("PARMS", 'LOCATION')

cmd1="ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
cmd2="hostname"
cmd3="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"

def run_cmd(cmd):
    p=Popen(cmd, shell=True, stdout=PIPE)
    output=p.communicate()[0]
    return output

def main():
    ipaddr = ''
    while ipaddr == '':
        ipaddr = run_cmd(cmd1)
    hostname = run_cmd(cmd2)
    droneid = run_cmd(cmd3)

    newstatus = 0
    while newstatus == 0:
        status = postData(str(loc).strip(' '), str(droneid).strip(' '))
        newstatus = status.doPost(str(ipaddr).strip(' '), str(hostname).strip(' '))



if __name__ == '__main__':
    main()
