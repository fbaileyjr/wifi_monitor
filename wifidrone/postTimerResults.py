#!/usr/bin/python -tt

import urllib
import urllib2
import wddx

import ConfigParser
url="http://nmsapp00.federated.fds/netops/ws/netops2.cfc?wsdl"
callmethod="postwifidroneresult"

class postResults:
    
    def __init__(self, loc, dronedata):
        self.droneid = dronedata
        self.location = loc
        
    def doPost(self, ssid, result1, result2, result3, details, myguid):
        
        try:
            params = urllib.urlencode({
                    'method': callmethod,
                    'location': self.location,
                    'droneid': self.droneid,
                    'ssid': ssid,
                    'test1result': result1,
                    'test2result': result2,
                    'test3result': result3,
		    'detail':  details,
                    'testguid': myguid
                    })
            response = urllib2.urlopen(url, params).read()
            return response
            print response
        except Exception as err:
        	print str(err)
        	return err
        	pass
    


