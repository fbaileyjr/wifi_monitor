sudo cp /tmp/hosts /etc/hosts
sleep 1
sudo cp /tmp/hostname /etc/hostname
sleep 1
sudo python /usr/share/drone/scripts/hostnameCheck/cronFile.py
sleep 2
