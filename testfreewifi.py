#! /usr/bin/python

from subprocess import *
#import subprocess
import time
from asynchttp import Http
from ssidParse import *
import urllib2, urllib, cookielib
import requests
from urlparse import urlparse
from BeautifulSoup import BeautifulSoup
import re
import httplib2

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
			
			#values = {'submit':'0'}
			#data = urllib.urlencode(values)
			cj = cookielib.CookieJar()
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			r = opener.open(url)
			#head = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
			#r = requests.get(url, headers=head)
			print r
			#print cj.name
			
			#print r
			#print r.headers
			#print r.headers['set-cookie']
			uparse = urlparse(r.url)
			print uparse.scheme
			print uparse.netloc
			print uparse.query
			#f = open('/home/pi/usercheck.txt', 'w')
			#f.write(r.text)
			#f.close()
			#response, content = http.request(url, 'GET', headers=head)
			#print response['content-location']
			#nexturl = response['content-location']
			#print response['set-cookie']
			time.sleep(2)
			#head = {'Content-type': 'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11','Cookie': r.headers['set-cookie']}
			head = cj.add_cookie_header(r)
			r2 = requests.post(r.url, headers=head)
			print r2.url
			print r2.headers
			#body = {'pre-check':'1', 'post-check':'1'}
			#headers = {'Content-type': 'application/x-www-form-urlencoded','User-Agent':'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11','Cookie': response['set-cookie']}
			#response2, content = http.request(url2, 'POST', headers=headers, body=urllib.urlencode(body))
			print r2
			print r2.url
			#headers = {'Cookie': response2['set-cookie']}
			time.sleep(2)
			r3 = requests.get(url, headers=head)
			print r3.headers
			#params = urllib.urlencode({'submit':0})
			
			#response = urllib2.urlopen(f,data)
			print r3
			print r3.url
			#print response.geturl()
			#print response.info()
			#print response.geturl()
			#h = urllib2.urlopen(url, timeout=10)
			#time.sleep(2)
			#print h.geturl()
			#print h.info()
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
	
	