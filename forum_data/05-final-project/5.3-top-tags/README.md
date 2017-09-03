## Top Tags

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

For an extra challenge you can think about how to get a top 10 list of tags, where they are ordered by some weighted score of your choice. If you decide to do this, then please submit your solution to the regular problem and then also submit this extra challenge problem in separate files as described on the instruction page.

### Hints for writing reducer code

Code should not use a data structure (e.g. a dictionary) in the reducer that stores a large number of keys. Remember that Hadoop already sorts the mapper output based on key, such that key-value pairs with the same key will appear consecutively as input to the reducer. Make sure you take advantage of this ordering when you write your reducer code.

Please feel free to use dictionaries to process data for the current key, but you shouldn't keep old data around from previous keys (eg. in a dictionary) if you don't need to.

This is part of a more general principle connected with the Volume characteristic of Big Data. Mappers and reducers read through very large amounts of data and we should be mindful, as we write mapper and reducer code, of how much data we store in main memory.
