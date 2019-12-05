#! /bin/bash

sudo tcpdump -i wlan0 -s 65535 -w /home/pi/sniffwlan.out
