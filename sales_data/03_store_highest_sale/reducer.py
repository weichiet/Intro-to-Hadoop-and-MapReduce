#!/usr/bin/python

import sys

maxSales = float("-inf")
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the item name, val is the sale amount
#
# All the sales for a particular item will be presented,
# then the key will change and we'll be dealing with the next item

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", maxSales
        oldKey = thisKey;
        maxSales = float("-inf")

    oldKey = thisKey
    if float(thisSale) > float(maxSales):
       maxSales = thisSale

if oldKey != None:
    print oldKey, "\t", maxSales
