#!/usr/bin/python3
"""import praw and  sys"""

import praw
import sys


def recurse(subreddit, hot_list=[], after=None):
    """with your actual Reddit API credentials"""
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT'
    )

    try:
        subreddit_obj = reddit.subreddit(subreddit)
        hot_posts = subreddit_obj.hot(limit=100, params={'after': after})

        for post in hot_posts:
            hot_list.append(post.title)

        after = hot_list[-1]

        return recurse(subreddit, hot_list, after)
    
    except Exception as e:
        print("An error occurred:", e)
        return None
