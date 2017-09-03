#!/usr/bin/python

#Find the number of hits for each different files on the website.

# Question to be answer:
# How many hits were made to the page /assets/js/the-associates.js?
# Answer: 2456

import sys

for line in sys.stdin:
    data = line.strip().split(" ")

    #print "{0}".format(len(data))
    if len(data) == 10:
        ip, identity, username, time, time_zone, method, page, http, status, size = data
        print "{0}\t{1}".format(page, 1)
