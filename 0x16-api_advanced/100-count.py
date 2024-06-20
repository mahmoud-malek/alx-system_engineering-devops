#!/usr/bin/python3

""" a recursive function that queries the Reddit API,
 parses the title of all hot articles,
 and prints a sorted count of given keywords
  (case-insensitive, delimited by spaces. Javascript should
   count as javascript, but java should not).
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
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
        if len(word_count) == 0:
            return
        for key in sorted(word_count, key=word_count.get, reverse=True):
            if word_count[key] != 0:
                print("{}: {}".format(key, word_count[key]))
        return
    for i in res.json()['data']['children']:
        title = i['data']['title'].lower().split()
        for word in word_list:
            word = word.lower()
            if word in title:
                if word in word_count:
                    word_count[word] += title.count(word)
                else:
                    word_count[word] = title.count(word)
    after = res.json()['data']['after']
    return count_words(subreddit, word_list, word_count, after)
