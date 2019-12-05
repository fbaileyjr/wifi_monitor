#!/usr/bin/python -tt
from runCmd import *
from shutil import *
import datetime


#function to write etc/contab
def crontabFile():
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
    + "*/5 *   * * *   pi      sudo /usr/share/drone/scripts/hostnameCheck/registerDrone.sh\n"
    + "#\n\n")
    
    #/etc/crontab file
    crontabOpen.close()
    
    try:
        run_cmd("sudo mv /tmp/crontab /etc/")
	return 1
    except:
        ef.write(datetime.datetime.now().ctime()+"\tCan't run the contrab command and replace file.\n")
        return 0
    #try:
    #    shutil.move("/tmp/hostname","/etc/hostname")
    #except:
    #    ef.write(datetime.datetime.now().ctime()+"\tCannot rename file. File doesn't exist.\n")
        

    ef.close()
