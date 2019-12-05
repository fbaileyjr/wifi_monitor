#!/bin/bash

sudo ifdown wlan0

sudo ifup wlan0=wlan_connect

MYSTATUS=`sudo wpa_cli status | grep wpa_state | awk -F '[=]+' '{print$2}'`

echo $MYSTATUS
if [ "$MYSTATUS" != "COMPLETED" ]; then
	WLANSTATUS=0
	WLANERROR=0
        AUTHCOUNTER=0
else
	WLANSTATUS=1
	WLANERROR=0
        AUTHCOUNTER=0
fi
#AUTHCOUNTER=0
while [[ $WLANSTATUS == 0 && $AUTHCOUNTER -lt 30 ]]; do
	MYSTATUS=`sudo wpa_cli status | grep wpa_state | awk -F '[=]+' '{print$2}'`
        
	if [ "$?" -eq "0" ] ; then
		#echo "successful"
		if [ "$MYSTATUS" != "COMPLETED" ]; then
        		sleep 1s
                        WLANSTATUS=0
			WLANERROR=0
                        AUTHCOUNTER=$[$AUTHCOUNTER+1]
		else
        		WLANSTATUS=1
			WLANERROR=0
		fi
	else
		echo "ERROR"
		WLANSTATUS=1
		WLANERROR=1
	fi
done
if [ $WLANSTATUS == 0 ]; then
    echo "Auth Problem"
else
    echo "DONE AUTHENTICATING"
    if [ $WLANERROR == 0 ]; then
	sudo dhclient wlan0 &
	MYIP=`sudo wpa_cli status | grep ip_address | awk -F '[=]+' '{print$2}'`
	COUNTER=0
	while [[ -z "$MYIP" &&  $COUNTER -lt 30 ]]; do
		sleep 1s
		MYIP=`sudo wpa_cli status | grep ip_address | awk -F '[=]+' '{print$2}'`
		echo $MYIP
		COUNTER=$[$COUNTER +1]
		#echo $COUNTER
	done

	if [ -z "$MYIP" ]; then
		echo "No DHCPOFFERS received"
	else
		echo $MYIP
		MESS="bound to $MYIP"
		echo $MESS
	fi
    else
	echo "No DHCPOFFERS received"
    fi
    
fi
exit

