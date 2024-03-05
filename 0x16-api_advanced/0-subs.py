#!/usr/bin/python3
"""
model holding the first task
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function
    should return 0.

    parameters:
    -----------
    subreddit: a string represent the subreddit

    return:
    -----------
    the total number of subscribers
    """
    headers = {"User-Agent": "ALX/1"}
    url = "https://www.reddit.com/"
    path = f"r/{subreddit}/about.json"
    number_subs = 0

    responce = requests.get(url+path, headers=headers, allow_redirects=False)

    if responce.status_code == 200:
        try:
            data = responce.json()['data']
            number_subs = data['subscribers']
        except Exception as e:
            return 0
    else:
        print(responce.status_code)

    return number_subs
