#!/bin/bash

sudo ifdown wlan0

sudo ifup wlan0=wlan_open

MYSTATUS=`sudo wpa_cli status | grep wpa_state | awk -F '[=]+' '{print$2}'`

echo $MYSTATUS
if [ "$MYSTATUS" != "COMPLETED" ]; then
	WLANSTATUS=0
	WLANERROR=0
else
	WLANSTATUS=1
	WLANERROR=0
fi

while [ $WLANSTATUS == 0 ]; do
	MYSTATUS=`sudo wpa_cli status | grep wpa_state | awk -F '[=]+' '{print$2}'`

	if [ "$?" -eq "0" ] ; then
		#echo "successful"
		if [ "$MYSTATUS" != "COMPLETED" ]; then
        		WLANSTATUS=0
			WLANERROR=0
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
echo "DONE CONNECTING"

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
exit
