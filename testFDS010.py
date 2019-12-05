#! /usr/bin/python

from subprocess import *
#import subprocess
import time
from ssidParse import *
import urllib2, urllib
from urlparse import urlparse
#import requests
from BeautifulSoup import BeautifulSoup
import re

cmd1 = "/usr/share/drone/scripts/wlanFDS010up.sh"
cmd2 = "/usr/share/drone/scripts/ethdown.sh"
cmd3 = "/usr/share/drone/scripts/networknormal.sh"

url = "http://www.google.com"
url2 = "http://mt000xsweb10"
url3 = "http://www.cnn.com"


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
    
    
    
    #linkregex = re.compile('<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')
    #links = linkregex.findall(msg)
    
    #for link in (links.pop(0) for _ in xrange(len(links))):
	#	if link.startswith('/'):
	#		#link = 'http://' + current_host + link
	#		print 'TYPE1:'
	#		print link
	#	elif link.startswith('#'):
	#		#link = 'http://' + current_host + current_uri + link
	#		print 'TYPE2:'
	#		print link
	#	elif not link.startswith('http'):
	#		#link = 'http://' + current_host + '/' + link
	#		print 'TYPE3:'
	#		print link
		
		#if link not in crawled:
		#	tocrawl.add(link)


def doFDS010Test():
	
	def run_cmd(cmd):
		p = Popen(cmd, shell=True, stdout=PIPE)
		output = p.communicate()[0]
		time.sleep(5)
		return output
		
	
	
	myconnect = run_cmd(cmd2)
	#time.sleep(10)
	myconnect2 = run_cmd(cmd1)
	#time.sleep(10)
	urlstatus = False
	while urlstatus == False:
		print 'CHECKING'
		try:
		
			#f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)
			response=urllib2.urlopen(url,timeout=5)
			print response.geturl()
			response2=urllib2.urlopen(url2,timeout=5)
			print response2.geturl()
			response3=urllib2.urlopen(url3,timeout=5)
			print response3.geturl()
			print 'Got Response'
			urlstatus = True
		except Exception as err:
			print str(err)
			pass
	
	print 'Looks Like I connected to FDS010'
	myconnect3 = run_cmd(cmd3)
	
	
	