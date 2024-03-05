#!/usr/bin/python3
"""
model that hold task 1 function
"""
import requests


def top_ten(subreddit):
    """queries the reddit API for the subreddit and find
    its top ten post
    parameter:
    -----------
    subreddit: str, text represents the subreddit title
    """
    url = "https://www.reddit.com/"
    path = f"r/{subreddit}/hot.json?limit=10&count=10"
    headers = {"User-Agent": "ALX/1"}
    posts_titles = []

    res = requests.get(url+path, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        try:
            # pprint.pprint(res.json())
            post_list = res.json()['data']['children']
            for idx, post in enumerate(post_list):
                if idx >= 10:
                    break;
                posts_titles.append(post['data']['title'])
        except Exception as e:
            posts_titles = None

        if posts_titles:
            for title in posts_titles:
                print(title)
    else:
        print(None)
