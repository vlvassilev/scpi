#!/usr/bin/python
import socket
import time
import datetime
import sys
from scpi import *
   
global fs

scpi_connect_serial('/dev/rfcomm0')

reply=query("STAT?")
print(reply)

reply=query("CONF?")
print(reply)

while 1:
    reply=query("FETC?")
    print(datetime.datetime.utcnow().strftime("%Y-%M-%dT%H:%M:%SZ"))
    reply=query("SYST:BATT?")
    print(reply)
    reply=cmd("SYST:BEEP")

    time.sleep(1)
