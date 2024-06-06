#!/usr/bin/python3
""" a module that contains a function that queries the Reddit
API and returns the number of subscribers
(not active users, total subscribers)"""

import requests


def number_of_subscribers(subreddit):
    """ a function that queries the Reddit API and returns
                 the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'linux:mahmoudmalek'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get('subscribers')
