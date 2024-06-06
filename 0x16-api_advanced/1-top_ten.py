#!/usr/bin/python3

""" Function to query the top ten hot posts on a given Reddit subreddit. """

import requests


def top_ten(subreddit):
    """ Return the top ten hot posts on a given subreddit. """
    url = "http://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": "linux: me"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code is not 200:
        print("None")
        return
    results = response.json().get("data").get("children")
    for post in results:
        print(post.get("data").get("title"))
    return
