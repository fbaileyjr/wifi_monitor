#! /bin/bash
# bash script to startup the drone.py script
#
# updated: 2020-Jan-26
# author: Frank Bailey
#


if [ "$(ps -eaf | grep -e [d]rone.py | awk '{print$2}')" == "" ]; then
        sudo python /usr/share/drone/wifidrone/drone.py
else
        sudo shutdown -rF now
fi
