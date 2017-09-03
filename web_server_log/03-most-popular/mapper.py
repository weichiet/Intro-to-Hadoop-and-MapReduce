#!/usr/bin/python

# Find the most popular file on the website.

# Some pathnames in the log begin with "http://www.the-associates.co.uk". 
# Besure to remove the portion "http://www.the-associates.co.uk" from pathnames in your
# mapper so that all occurences of a file are counted together.


import sys
import re

for line in sys.stdin:
    data = line.strip().split(" ")

    if len(data) == 10:
        ip, identity, username, time, time_zone, method, page, http, status, size = data
        cleaned_path = re.sub(r"^http://www.the-associates.co.uk", '', page)
	print "{0}\t{1}".format(cleaned_path, 1)    



