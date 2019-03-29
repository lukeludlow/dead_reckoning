#!/bin/bash

udevadm info -a -p $(udevadm info -q path -n $1)

# example usage:
# udevadm info -a -p $(udevadm info -q path -n /dev/ttyACM0)
