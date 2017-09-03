#!/usr/bin/python

#Find the number of hits to the site made by each different IP address

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    
    #print "{0}".format(len(data))
    if len(data) == 10:
        ip, identity, username, time, time_zone, method, page, http, status, size = data
        print "{0}\t{1}".format(ip, 1)    



