#! /bin/bash

if [ "$(ps -eaf | grep -e [d]rone.py | awk '{print$2}')" == "" ]; then
        sudo python /usr/share/drone/wifidrone/drone.py
else
        sudo shutdown -rF now
fi
