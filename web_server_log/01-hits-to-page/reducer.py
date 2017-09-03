#!/usr/bin/python

#Find the number of hits for each different files on the website.
import sys

visitsTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisVisit = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", visitsTotal
        oldKey = thisKey;
        visitsTotal = 0

    oldKey = thisKey
    visitsTotal += float(thisVisit)

if oldKey != None:
    print oldKey, "\t", visitsTotal
