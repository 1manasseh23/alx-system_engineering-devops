#!/usr/bin/python3
"""
This a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a
given subreddit
"""
import praw
import prawcore


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If not a valid subreddit, prints None
    """
    if hot_list is None:
        hot_list = []
    reddit = praw.Reddit(
            client_id='YOUR_CLIENT_ID',
            client_secret='YOUR_CLIENT_SECRET',
            user_agent='YOUR_USER_AGENT')
    try:
        subreddit_obj = reddit.subreddit(subreddit)
        hot_articles = subreddit_obj.hot(limit=100, params={'after': after})
        for article in hot_articles:
            hot_list.append(article.title)
        if hot_articles._listing:
            return recurse(
                    subreddit,
                    hot_list,
                    hot_articles._listing[-1].fullname)
        else:
            if hot_list:
                return hot_list
            else:
                return None
    except prawcore.exceptions.ResponseException as e:
        return None
