## Study Groups
We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.


### Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.
