#! /usr/bin/python

from subprocess import *
#import subprocess
import time, ConfigParser
from ssidParse import *
import urllib2, urllib
from urlparse import urlparse
#import requests
from BeautifulSoup import BeautifulSoup
import re

def doConnTest(url, interval):
	
	try:
		response=urllib2.urlopen(url,timeout=interval)
		#print response.geturl()
		myresult = '1'
	except Exception as err:
		myresult=str(err)
		#print str(err)
	
	return myresult