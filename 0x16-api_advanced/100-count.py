#!/usr/bin/python3
"""
python model that hold task 3
"""
import requests
from operator import itemgetter


def count_words(subreddit, word_list, word_dict={}, after=''):
    """
    count the number of accuranes of the word_list words on
    all tha hot post titles for the subredditr recusrivly
    """

    url = "https://www.reddit.com/"
    path = f"r/{subreddit}/hot.json?count=1&limit=1&after={after}"
    headers = {"User-Agent": "ALX/1"}

    res = requests.get(url+path, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        try:
            post = res.json()['data']['children'][0]
            title = post['data']['title']
            title = title.lower().split()
            for word in word_list:
                if word.lower() in title:
                    word_dict[word.lower()] += word_dict.get(word.lower(), 0) + 1
            after = post['data']['name']
            try:
                sorted_dict = dict(sorted(word_dict.items(), key=itemgetter(0, 1)))
            except Exception as e:
                sorted_dict = word_dict
            word_dict = count_words(subreddit, word_list, word_dict=sorted_dict, after=after)
        except Exception as e:
            # pass

    else:
        #count_words(subreddit, word_list, word_dict=word_dict, after=after)
        return word_dict
    for key, val in word_dict.items():
        print("{}: {}".format(key, value))
    #word_dict = {}
