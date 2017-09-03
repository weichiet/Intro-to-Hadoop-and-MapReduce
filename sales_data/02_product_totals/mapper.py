#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 3 (item name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

# Questions to be answered:
# What is the value of total sales for the following categories
# Toys: 57463477.11
# Consumer Electronics: 57452374.13

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)
