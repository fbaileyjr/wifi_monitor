#!/usr/bin/python -tt

import urllib
import urllib2
from runCmd import *
from subprocess import *

url="http://nmsapp00.federated.fds/netops/ws/netops2.cfc?wsdl"

#function to get info from webserver
def doPost(did, cmethod):

    try:
        params = urllib.urlencode({
            'method': cmethod,
            'droneid': did
            })
        response = urllib2.urlopen(url, params).read()
        return response;
        print response
    except Exception as err:
        print str(err)
        print "Error"
        return 0
        pass
