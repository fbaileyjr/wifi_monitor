import syslog
from runCmd import *
from shutil import *
from removeCert import *
import datetime


def startDrone():    
    try:
        run_cmd("sudo python /usr/share/drone/dronestart.py")
        return 1
    except Exception as err:
        syslog.syslog(syslog.LOG_ERR, err)
        return 0
    
def startPuppetTest():
    try:
        run_cmd("sudo puppet agent --test")
        return 1
    except Exception as err:
        syslog.syslog(syslog.LOG_ERR, err)
        return 0

def startPuppet(): 
    try:
        run_cmd("sudo puppet agent")
        return 1
    except Exception as err:
        syslog.syslog(syslog.LOG_ERR, err)
        return 0

def hostnameDirRemoval(): 
    try:
        run_cmd("sudo rm -r /usr/share/drone/scripts/hostnameCheck")
        return 1
    except Exception as err:
        syslog.syslog(syslog.LOG_ERR, err)
        return 0

def replaceFinalCron():
    crontab = "/tmp/crontab"
    errorfile = "/var/log/pythonerrors.log"
    
    crontabOpen = open(crontab , "wb")
    ef = open(errorfile, "wb")
    
    print "writing crontab file "
    crontabOpen.write ("# /etc/crontab: system-wide crontab\n"
    + "# Unlike any other crontab you don't have to run the `crontab'\n"
    + "# command to install the new version when you edit this file\n"
    + "# and files in /etc/cron.d. These files also have username fields,\n"
    + "# that none of the other crontabs do.\n"
    + "SHELL=/bin/sh\n"
    + "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n\n"

    + "# m h dom mon dow user  command\n"
    + "17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly\n"
    + "25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )\n"
    + "47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )\n"
    + "52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )\n"
    + "#*/15 * * * *   pi      sudo /usr/share/drone/startup.sh\n"
    + "10 0    * * *   pi      sudo shutdown -rF now\n"
    + "#15 7   * * *   pi      sudo shutdown -rF now\n"
    + "*/5 *   * * *   pi      sudo puppet agent\n"
    + "#\n\n")
    
    #/etc/crontab file
    crontabOpen.close()
    
    try:
        run_cmd("sudo mv /tmp/crontab /etc/")
    except:
        ef.write(datetime.datetime.now().ctime()+"\tCan't run the contrab command and replace file.\n")
        
    #try:
    #    shutil.move("/tmp/hostname","/etc/hostname")
    #except:
    #    ef.write(datetime.datetime.now().ctime()+"\tCannot rename file. File doesn't exist.\n")
        

    ef.close()
        
myTest1 = startDrone()
myTest2 = 0
myTest3 = 0
host = run_cmd("sudo cat /etc/hostname")


if myTest1 == 1 and host != "me000drone01":
    ssh_connect()
    myTest2 = startPuppetTest()
else:
    syslog.syslog(syslog.LOG_ERR, "Dronestart File does not exist")
    pass

if myTest2 == 1:
    run_cmd("sudo /etc/rc.local")
    run_cmd("sudo puppet agent")
    replaceFinalCron()
    hostnameDirRemoval()
    run_cmd("sudo shutdown -r 1")
else:
    syslog.syslog(syslog.LOG_ERR, "Could not delete directory, does not exist")
    pass
