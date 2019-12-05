#! /usr/bin/python



def doSSIDParse(data):
	
	def foo(s, leader, trailer):
		end_of_leader = s.index(leader) + len(leader)
		start_of_trailer = s.index(trailer, end_of_leader)
		return s[end_of_leader:start_of_trailer]
	
	gdata = data.split('\n')
	linecount = 0
	for line in gdata:
		if line != '':
			line2 = line.split(' ')
			linecount = linecount + 1
			count = 0
			for newdata in line2:
				count = count + 1
				if count == 1:
					ap=newdata
				elif count == 2:
					try:
						ssid = foo(newdata, '"','"')
					except Exception as err:
						ssid = 'ukn'
					if ssid == '':
						ssid = 'hidden'
				elif count == 3:
					freq = newdata
				elif count == 4:
					qual = newdata
				elif count == 5:
					sig = newdata
			if sig != '0':
				print "AP:" + str(ap).replace(':','.'), "SSID:" + str(ssid), "FREQUENCY:" + str(freq), "QUALITY:" + str(qual), "SIGNAL:" + str(sig)
				

