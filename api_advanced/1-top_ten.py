#!/usr/bin/python3
"""
This module defines a function to print the titles of
the top 10 hot posts from a given subreddit.
"""

import requests


def top_ten(subreddit):
        """
        Prints the titles of the first 10 hot posts for a given subreddit.
        If the subreddit is invalid, prints None.
        """
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {'User-Agent': 'CustomUserAgent/1.0'}

        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))                                                        
