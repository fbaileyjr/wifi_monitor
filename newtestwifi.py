#! /usr/bin/python

from subprocess import *
#import subprocess
import time
from ssidParse import *
import urllib2, urllib, cookielib
import requests
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup
import re
import mechanize

cmd1 = "sudo ifup wlan0=wlan_open"
cmd2 = "sudo ifdown eth0"
cmd3 = "sudo ifdown wlan0 && sudo ifup eth0"

url = "http://www.google.com"
url2 = "http://11.48.59.1/UserCheck/data/GetUserCheckIncidentData"
url3 = "http://11.48.59.1/UserCheck/data/GetUserCheckUserChoiceData"


def getURL(msg):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    soup = BeautifulSoup(msg)
    links = soup.find_all('http:')
    for tag in links:
    	link = tag.get('//',None)
    	if link != None:
    		print link
    

def doTest():
	
	def run_cmd(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		time.sleep(5)
		return output
		
	def run_cmd2(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		time.sleep(5)
		return output
	
	
	myconnect = run_cmd2(cmd2)
	#time.sleep(10)
	myconnect2 = run_cmd(cmd1)
	#time.sleep(10)
	urlstatus = False
	while urlstatus == False:
		print 'CHECKING'
		try:
			
			mytest1 = doConnTest(url,2)
			if mytest1 == '1':
				print 'GOOD for 2 seconds\n'
				##doPostResults()
			else:
				print mytest1
				mytest2 = doConnTest(url,5)
				if mytest2 == '1':
					print 'GOOD for 5 seconds\n'
					##doPostResults()
				else:
					print mytest2
					mytest3 = doConnTest(url,10)
					if mytest3 == '1':
						print 'GOOD for 10 seconds\n'
						##doPostResults()
					else:
						print url, 'FAILED ALL TESTS'
						print mytest3
						##doPostResults()
			
			print 'Got Response'
			urlstatus = True
		except urllib2.URLError as err:
			print str(err)
			pass
	
	#myresponse = response.read()
	# parse html
	#page = str(BeautifulSoup(myresponse))
	#getURL
	print 'Looks Done'
	myconnect3 = run_cmd(cmd3)
	#print myresponse
	
	
	#html = response.read()
	#myurls = urlparse(html)
	#myurls.geturl()
	#print myurls
	#print html
	#myhtml = html.split(';')
	#for line in myhtml:
	#	print '>>' + str(line)
	
	