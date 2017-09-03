#!/usr/bin/python
import sys
import csv
import re

# Write a Mapreduce program that creates an index of all words that can be found in the body of forum posts, and the node they were found in.
# Do not parse HTML. Split the text on all whitespace, as well as the following characters: .!?:;"()<>[]#$=~/

# Questions that should be answerable:
# How many times was the word 'fantastic' used in forums?
# Answer: 345

# List of comma separated nodes where the word fantastically can be found. List the nodes in ascending order (1,2,3,4,5...)
# Answer: 17583, 1007765, 1025821, 7004477, 9006895


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
    	try:
	        id = int(line[0].strip())
	        body = line[4]
	        words = filter(bool, [word.strip() for word in re.split('[^a-zA-Z0-9\']+', body)])

	        for word in words:
	            print word.lower(),id
        except ValueError:
        	continue

if __name__ == "__main__":
    mapper()
