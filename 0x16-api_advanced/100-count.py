#!/usr/bin/python3
"""
python model that hold task 3
"""
import requests


def count_words(subreddit, word_list, word_dict={}, after=''):
    """
    count the number of accuranes of the word_list words on
    all tha hot post titles for the subredditr recusrivly
    """

    url = "https://www.reddit.com/"
    path = f"r/{subreddit}/hot.json?after={after}&count=1"
    headers = {"User-Agent": "ALX/1"}

    res = requests.get(url+path, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        try:
            post = res.json()['data']['children'][0]
            title = post['data']['title']
                for word in word_list:
                    if word.lower() in title.lower():
                        word_dict[word.lower()] += word_dict.get(word.lower(), 0) + 1
            after = post['data']['name']

