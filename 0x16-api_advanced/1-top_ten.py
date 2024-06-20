#!/usr/bin/pyhon3

""" a function that queries the Reddit API
 and prints the titles of the first 10 hot
  posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """ this is a function to get the top ten
                    posts in a subreddit
                    """
    headers = {"User-Agent": "Linux: Mahmoud malek"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(None)
        return
    for i in range(10):
        print(res.json()['data']['children'][i]['data']['title'])
