#!/usr/bin/python3

"""  a function that queries the Reddit API and returns the number
 of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the
"""

import requests


def number_of_subscribers(subreddit):
    """ this is a function to get the number of
            subcribers to a subreddit
            """
    headers = {"User-Agent": "Linux: Mahmoud malek"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        return 0
    return res.json()['data']['subscribers']
