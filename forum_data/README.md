# Forum Data

This particular dataset was taken from the Udacity forums the first months after the launch of this course. Udacity forums were run on a free, opensource software called OSQA, which was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.

The dataset can be downloaded [here](https://www.dropbox.com/s/ib0j7xkx88m0i0r/forum_data.tar.gz?dl=0). There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes. You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

* "id": id of the node
* "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
* "tagnames": space separated list of tags
* "author_id": id of the author
* "body": content of the post
* "node_type": type of the node, either "question", "answer" or "comment"
* "parent_id": node under which the post is located, will be empty for "questions"
* "abs_parent_id": top node where the post is located
* "added_at": date added

The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. The actual database has more fields in this table, like user name nickname, bio (if set) etc, but we have removed this information here.


## List of Questions
1. [Count the number of forum nodes where "body" satisfy certain pattern.](./01-filtering-exercise)
2. [Print out 10 lines containing longest posts, sorted in ascending order from shortest to longest.](./02-top-10)
3. [Create an index of all words that can be found in the body of forum posts, and the node they were found in.](./03-invertes-index)
4. [Combine forum data and user data.](./04-combined-datasets)

Besides the above 4 questions, the [final project](./05-final-project) of this course also uses this dataset.
