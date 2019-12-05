#! /usr/bin/python

from subprocess import *
import smbus
import subprocess
import re
import socket
import fcntl
import struct
import paramiko
import signal
#import subprocess
import time, ConfigParser
from ssidParse import *
import urllib2, urllib
from urlparse import urlparse
#import requests
from BeautifulSoup import BeautifulSoup
from conntest import *
from postTestResults import postResultsData
from myexception import *


def doWifiTest(typetest, guid):
	
	def get_gateway(ifname):
		proc = subprocess.Popen("ip route list dev " + ifname + " | awk ' /^default/ {print $3}'", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		return_code = proc.wait()
		for line in proc.stdout:
			line
		return line
		
	def get_ip_address(ifname):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		return socket.inet_ntoa(fcntl.ioctl(
			s.fileno(),
			0x8915,  # SIOCGIFADDR
			struct.pack('256s', ifname[:15])
		)[20:24])
		
	def ping_gw():
		ip_gateway = get_gateway('wlan0')
 
		proc = subprocess.Popen("ping -c 2 " + ip_gateway + " 2>&1", shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
 
		return_code = proc.wait()
 
		# Read from pipes
		# stdout
		for line in proc.stdout:
		   if "loss" in line:
			   packet_loss = re.search('\d*%',line).group()
			   if int(packet_loss.split('%')[0]) > 0:
				   print("Ping Gateway:\nFailed")
				   time.sleep(1)
				   return False
				   #print ip_gateway + packet_loss + " packet loss for gateway." 
			   else:
				   
				   print("Ping Gateway:\nSuccess")
				   time.sleep(1)
				   return True
				   #print "Gateway is reachable"  
		# stderr
		for line in proc.stderr:
			print("stderr: " + line.rstrip())
			
	
	
	config = ConfigParser.RawConfigParser()
	config.read('/usr/share/drone/drone.conf')
	loc = config.get("PARMS", 'LOCATION')
	test1 = config.get("TESTSCRIPTS", typetest)
	url = config.get(typetest, "1")
	url2 = config.get(typetest, "2")
	url3 = config.get(typetest, "3")
	testresults = {}
	
	if typetest == "FDS010":
		cmd = "/usr/share/drone/scripts/wlanFDS010up.sh"
		cmd1 = "/usr/share/drone/scripts/ethdown.sh"
		cmd2 = "/usr/share/drone/scripts/networknormal.sh"
		cmd3="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"
	elif typetest == "FDS030":
		cmd = "/usr/share/drone/scripts/wlanFDS030up.sh"
		cmd1 = "/usr/share/drone/scripts/ethdown.sh"
		cmd2 = "/usr/share/drone/scripts/networknormal.sh"
		cmd3="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"
	elif typetest == "FREEWIFI":
		cmd = "/usr/share/drone/scripts/wlanFREEup.sh"
		cmd1 = "/usr/share/drone/scripts/ethdown.sh"
		cmd2 = "/usr/share/drone/scripts/networknormal.sh"
		cmd3="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"
	elif typetest == "OMNI":
		cmd = "/usr/share/drone/scripts/wlanOMNIup.sh"
                cmd1 = "/usr/share/drone/scripts/ethdown.sh"
                cmd2 = "/usr/share/drone/scripts/networknormal.sh"
                cmd3="cat /proc/cpuinfo | grep Serial | awk '{print $3}'"	
	
	def run_cmd(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		time.sleep(5)
		return output
	
	def run_command(cmd):
		p = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        	return iter(p.stdout.readline, b'')
		
	

	myconnect = run_cmd(cmd1)
	#time.sleep(10)
	#myconnect2 = run_cmd(cmd)
	for line in run_command(cmd):
        	connect = 0
        	if line.startswith('bound to'):
                	connect = 1
        	elif line.startswith('No DHCPOFFERS received'):
                	connect = 0
	
	print 'CONNECT: ' + str(connect)
	#time.sleep(10)
	if connect == 1:
                mynewip = get_ip_address('wlan0')
                iptries = 0
                try:
                        while mynewip == '':
                                mynewip = get_ip_address('wlan0')
                                iptries += 1
                                if iptries <= 5:
                                        time.sleep(2)
                                else:
                                        results1 = [2,2,2]
                                        results2 = [2,2,2]
                                        results3 = [2,2,2]
                                        raise NoIPException
                                        
                        urlstatus = False
                        mygw = get_gateway('wlan0')
                        print mygw
                        mygwping = ping_gw()
                        print mygwping
                        
                        while urlstatus == False:
                                print 'CHECKING'
                                try:
                                        results1 = []
                                        mytest1 = doConnTest(url,2)
                                        if mytest1 == '1':
                                                print 'GOOD for 2 seconds\n'
                                                ##doPostResults()
                                                results1 = [1,1,1]
                                        else:
                                                print mytest1
                                                
                                                mytest2 = doConnTest(url,5)
                                                if mytest2 == '1':
                                                        print 'GOOD for 5 seconds\n'
                                                        ##doPostResults()
                                                        results1 = [0,1,1]
                                                else:
                                                        print mytest2
                                                        
                                                        mytest3 = doConnTest(url,10)
                                                        if mytest3 == '1':
                                                                print 'GOOD for 10 seconds\n'
                                                                ##doPostResults()
                                                                results1 = [0,0,1]
                                                        else:
                                                                print url, 'FAILED ALL TESTS'
                                                                print mytest3
                                                                ##doPostResults()
                                                                results1 = [0,0,0]
                                                
                                        results2 = []
                                        mytest1 = doConnTest(url2,2)
                                        if mytest1 == '1':
                                                print 'GOOD for 2 seconds\n'
                                                results2 = [1,1,1]
                                                ##doPostResults()
                                        else:
                                                print mytest1
                                                mytest2 = doConnTest(url2,5)
                                                if mytest2 == '1':
                                                        print 'GOOD for 5 seconds\n'
                                                        ##doPostResults()
                                                        results2 = [0,1,1]
                                                else:
                                                        print mytest2
                                                        mytest3 = doConnTest(url2,10)
                                                        if mytest3 == '1':
                                                                print 'GOOD for 10 seconds\n'
                                                                results2 = [0,0,1]
                                                                ##doPostResults()
                                                        else:
                                                                print url2, 'FAILED ALL TESTS'
                                                                print mytest3
                                                                ##doPostResults()
                                                                results2 = [0,0,0]
                                        
                                        results3 = []
                                        mytest1 = doConnTest(url3,2)
                                        if mytest1 == '1':
                                                print 'GOOD for 2 seconds\n'
                                                results3 = [1,1,1]
                                                ##doPostResults()
                                        else:
                                                print mytest1
                                                mytest2 = doConnTest(url3,5)
                                                if mytest2 == '1':
                                                        print 'GOOD for 5 seconds\n'
                                                        results3 = [0,1,1]
                                                        ##doPostResults()
                                                else:
                                                        print mytest2
                                                        mytest3 = doConnTest(url3,10)
                                                        if mytest3 == '1':
                                                                print 'GOOD for 10 seconds\n'
                                                                results3 = [0,0,1]
                                                                ##doPostResults()
                                                        else:
                                                                print url3, 'FAILED ALL TESTS'
                                                                print mytest3
                                                                results3 = [0,0,0]
                                                                ##doPostResults()
                                                        
                                        
                                        print 'Got Response'
                                        mystatuscode = 'Connection Passed'
                                        urlstatus = True
                                except Exception as err:
                                        print str(err)
                                        pass
                except NoIPException:
                        print 'Got NoIPException'
                        mystatuscode = 'Failed on IP'
        else:
                urlstatus = True
                mystatuscode = 'DHCP FAILURE'
                results1 = [9,9,9]
                results2 = [9,9,9]
                results3 = [9,9,9]
	
	print mystatuscode, str(typetest)
	myconnect3 = run_cmd(cmd2)
	dronedata = run_cmd(cmd3)
	print results1
	print results2
	print results3
	status = postResultsData(str(loc).strip(' '), str(dronedata).strip(' '))
	newrsult1 = status.doPost(1, typetest, results1[0], results1[1], results1[2], guid)
	newrsult2 = status.doPost(2, typetest, results2[0], results2[1], results2[2], guid)
	newrsult3 = status.doPost(3, typetest, results3[0], results3[1], results3[2], guid)
	
	
	
	
	
	
