#!/bin/python
import re;

from sys import argv

current_file = open ('/var/log/message');
iplist = "";

for line in current_file:
	if "Failed" in line:
		ip = ''.join(re.findall( r'[0-9]+(?:\.[0-9]+){3}', line ))
		if ip not in iplist:
			iplist = iplist + " " +ip;

print iplist;

#print current_file.readline()
