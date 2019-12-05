#! /usr/bin/python

import httplib
import sys
import time

default_timer = time.time

def doConnTest(url, interval):
    path = '/'

    try:
        conn = httplib.HTTPConnection(url, timeout=10)
        goodconn = 1
    except Exception as e1:
        print str(e1)
        goodconn = 0
    if goodconn == 1:
        start = default_timer()
        try:
            conn.request('GET', path,)
            #request_time = default_timer()
            resp = conn.getresponse()
            response_time = default_timer()
            size = len(resp.read())
            conn.close()
            transfer_time = default_timer()
            tran_time = transfer_time - start
            return [tran_time,'0']
            print '%.5f content transferred (%i bytes)' % ((tran_time), size)
        except Exception as e2:
            return [99,str(e2)]
            print str(e2)
            print 'TEST FAILED'
    else:
        return [999,str(e1)]
        print 'TEST FAILED'
