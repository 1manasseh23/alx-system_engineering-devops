#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If not a valid subreddit, prints None.
    """
    # Set a custom User-Agent to avoid rate limiting
    headers = {'User-Agent': 'MyApp/0.0.1'}

    try:
        # Make a GET request to the Reddit API for the given subreddit
        response = requests.get(
                f'https://www.reddit.com/r/{subreddit}/hot.json',
                headers=headers)

        if response.status_code == 200:
            data = response.json()

            if 'data' in data and 'children' in data['data']:
                for post in data['data']['children'][:10]:
                    print(post['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except (requests.exceptions.RequestException, KeyError):
        print(None)
