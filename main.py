#!/usr/bin/python
import praw
import pdb
import re
import os
reddit = praw.Reddit('bot1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "a") as f:
        posts_replied_to = f.read()
        posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit("hmmm")

for submission in subreddit.hot():
    if submission.id not in posts_replied_to:
            if re.search("hmmm", submission.title, re.IGNORECASE):
                posts_replied_to.append(submission.id)
                submission.reply("This is so hmmy hmmm.")
                with open("posts_replied_to.txt", "w") as f:
                    for post_id in posts_replied_to:
                        f.append(post_id + "\n")
