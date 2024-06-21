#!/usr/bin/python3

"""  a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
 If no results are found for the given subreddit,
  the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ this is a function to get the top ten
                                        posts in a subreddit
                                        """
    headers = {"User-Agent": "Linux: Mahmoud malek"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:
        url = url + '?after=' + after
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        return None
    if res.json()['data']['children'] == []:
        return hot_list
    for i in res.json()['data']['children']:
        hot_list.append(i['data']['title'])
    after = res.json()['data']['after']
    return recurse(subreddit, hot_list, after)
