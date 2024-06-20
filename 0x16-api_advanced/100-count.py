#!/usr/bin/python3

""" a recursive function that queries the Reddit API,
 parses the title of all hot articles,
 and prints a sorted count of given keywords
  (case-insensitive, delimited by spaces. Javascript should
   count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list):
    """ this is a function to get the top ten
                                    posts in a subreddit
                                    """
    headers = {"User-Agent": "Linux: Mahmoud malek"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(None)
        return
    hot_list = []
    for i in res.json()['data']['children']:
        hot_list.append(i['data']['title'])
    for i in word_list:
        count = 0
        for j in hot_list:
            count += j.lower().split().count(i.lower())
        if count != 0:
            print("{}: {}".format(i, count))
    return
