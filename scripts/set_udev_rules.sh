#!/bin/bash

echo "start copy udev rules to  /etc/udev/rules.d/"
printf "copying ./*.rules to /etc/udev/rules.d/\n"
sudo cp ./*.rules /etc/udev/rules.d
printf "reloading udev\n"
sudo udevadm control --reload-rules
sudo service udev restart
sudo udevadm trigger
printf "done\n"
