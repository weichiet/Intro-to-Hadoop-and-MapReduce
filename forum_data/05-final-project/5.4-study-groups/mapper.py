#!/usr/bin/env python

"""
Study Groups

We might want to help students form study groups.
But first we want to see if there are already students on forums that communicate a lotbetween themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread
(that is a question node with all it's answers and comments) would give us a list of students that have posted there
- either asked the question, answered a question or added a comment.
If a student posted to that thread several times, they should be added to that
list several times as well, to indicate intensity of communication.
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if len(line) == 19:
        if not line[0].isdigit():
            continue

        node_id, title, tag_names, author_id, body, node_type, parent_id, abs_parent_id, added_at, score = line[0:10]

        if node_type == "question":
            identifier = node_id
        else:
            identifier = abs_parent_id

        print "{0}\t{1}".format(identifier, author_id)
