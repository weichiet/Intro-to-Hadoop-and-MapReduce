#!/usr/bin/python

# Find the most popular file on the website.


import sys

visitsTotal = 0
oldKey = None

mostVisitedPage = None
mostVisitedTotal = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVisit = data_mapped

    if oldKey and oldKey != thisKey:
    	if visitsTotal > mostVisitedTotal:
    	   mostVisitedTotal = visitsTotal
    	   mostVisitedPage = oldKey

            oldKey = thisKey;
            visitsTotal = 0

    oldKey = thisKey
    visitsTotal += float(thisVisit)

if oldKey != None:
   if visitsTotal > mostVisitedTotal:
      mostVisitedTotal = visitsTotal
      mostVisitedPage = oldKey

if mostVisitedPage != None:
   print mostVisitedPage, "\t", mostVisitedTotal
