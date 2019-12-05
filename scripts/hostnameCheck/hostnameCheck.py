#!/usr/bin/python -tt

import wddx
import re
import datetime
import ConfigParser
import shutil
import syslog
from callWebsite import *
from fileProcess import *
from subprocess import *
from runCmd import *
from cronFile import *




#variables for run_cmd(cmd)
cmd="sudo cat /proc/cpuinfo | grep Serial | awk '{print $3}'"

#variables for doPost function
callmethod="provision"


#processedString = re.sub(r'<.*?>+',r'', returnString)
droneid = run_cmd(cmd)
droneid = droneid.strip()

#print droneid

returnString = doPost(droneid, callmethod)
hostname = wddx.loads(returnString)

fun1 = 1
fun2 = 1
fun3 = 1
    
if hostname[0] != "0" and hostname[0] != "me000drone01":
    fun1 = hostnameFile(hostname[0])
else:
    syslog.syslog(syslog.LOG_ERR, "Hostname is not found")
    pass

if fun1 == 1:
    fun2 = crontabFile()
else:
    syslog.syslog(syslog.LOG_ERR, "Hostname Process failed")
    pass

if fun2 == 1:
    run_cmd("sudo shutdown -r 1")
else:
    pass
