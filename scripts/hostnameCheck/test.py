from removeCert import *
from runCmd import *
import pxssh
import getpass
import pexpect

host = run_cmd("sudo cat /etc/hostname")
host = host.strip()

try:                                
    s = pxssh.pxssh()
    hostname = 'nmsapp00'
    username = 'netops'
    password = 'pepelapew1'
    s.login (hostname, username, password)
    s.sendline ('uptime')  # run a command
    s.prompt()         # match the prompt
    print s.before     # print everything before the prompt.
    s.sendline ('sudo puppet cert clean ' + host + '.federated.fds')
    ret = s.expect([pexpect.TIMEOUT, '\[sudo\] password for netops:'])
    if ret == 0:
        print('Command is not found')
    if ret == 1:
        s.sendline(password)
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)




