#!/usr/bin/python3
"""
This a function that queries the Reddit API,
parses the title of all hot articles, and prints a
sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count
as javascript, but java should not)
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    function named count_words that takes four parameters.
    subreddit:
            The name of the subreddit to query
    word_list:
            A list of keywords to count occurrences of in the
            subreddit's posts.
    after:
            (Optional) The ID of the last post seen in a previous request.
            This is used for pagination.
    count_dict:
            (Optional) A dictionary to store the counts of each keyword.
            This parameter is used for recursion and should not be supplied
            when calling the function.
    """
    if count_dict is None:
        count_dict = {}

    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"

    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("Invalid subreddit or no posts match.")
        return

    data = response.json()

    children = data["data"]["children"]

    for child in children:
        title = child["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1

    after = data["data"]["after"]
    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")

