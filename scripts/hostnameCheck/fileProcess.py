from runCmd import *
from shutil import *
import datetime


#function to write etc/hosts and etc/hostname file
def hostnameFile(hostvar):
    hostname = hostvar
    ehosts = "/tmp/hosts"
    ehostname = "/tmp/hostname"
    errorfile = "/var/log/pythonerrors.log"
    
    ehostsOpen = open(ehosts, "wb")
    ehostnameOpen = open(ehostname, "wb")
    ef = open(errorfile, "wb")
    
    print "writing ehost file " + hostname
    ehostsOpen.write ("127.0.0.1       localhost\n\n"
    + "# The following lines are desirable for IPv6 capable hosts\n\n"
    + "::1     ip6-localhost ip6-loopback\n"
    + "fe00::0\tip6-localnet\n"
    + "ff00::0\tip6-mcastprefix\n"
    + "ff02::1\tip6-allnodes\n"
    + "ff02::2\tip6-allrouters\n\n"
    + "127.0.1.1\t" + hostname + "\n")
    
    #/etc/hostname file
    ehostnameOpen.write(hostname)
    ehostsOpen.close()
    ehostnameOpen.close()
    
    try:
	run_cmd("sudo /usr/share/drone/scripts/hostnameCheck/moveFiles.sh")
    	return 1
    except:
        ef.write(datetime.datetime.now().ctime()+"\tCan't run the command and replace file.\n")
        return 0
    #try:
    #    shutil.move("/tmp/hostname","/etc/hostname")
    #except:
    #    ef.write(datetime.datetime.now().ctime()+"\tCannot rename file. File doesn't exist.\n")
        

    ef.close()
