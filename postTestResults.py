# this is used to post the results to the remote web server
#!/usr/bin/python -tt

import urllib
import urllib2
import wddx

import ConfigParser
url="<enter_ssid>"
callmethod="postdronewifiresult"

class postResultsData:

    def __init__(self, loc, dronedata):
    	
        self.droneid = dronedata
        self.location = loc

    def doPost(self, testnum, ssid, result1, result2, result3,myguid):
        
        try:
            params = urllib.urlencode({
                    'method': callmethod,
                    'location': self.location,
                    'droneid': self.droneid,
                    'ssid': ssid,
                    'testnumber': testnum,
                    'test1result': result1,
                    'test2result': result2,
                    'test3result': result3,
                    'testguid': myguid
                    })
            response = urllib2.urlopen(url, params).read()
            return response
            print response
        except Exception as err:
        	print str(err)
        	return 0
        	pass
