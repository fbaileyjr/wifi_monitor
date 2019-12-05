#! /bin/bash


if [ "$(sudo cat /etc/hostname)" != "me000drone01" ]; then
        echo "Hostname has been renamed"
else
        sudo python /usr/share/drone/scripts/hostnameCheck/hostnameCheck.py
fi

