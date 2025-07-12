#!/usr/bin/python3
"""
This module defines a recursive function that queries the Reddit API
and returns a list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
        """
            Recursively queries the Reddit API and returns a list containing 
            the titles of all hot articles for a given subreddit.

            Args:
                subreddit (str): The name of the subreddit.
                hot_list (list): Accumulator for hot post titles.
                after (str): Token for next page of results (for pagination).

            Returns:
                list: A list of titles of hot posts, or None if subreddit is invalid.
            """
            url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
            headers = {'User-Agent': 'CustomUserAgent/1.0'}
            params = {'limit': 100, 'after': after}

            response = requests.get(url, headers=headers, params=params, allow_redirects=False)

            if response.status_code != 200:
                return None

            data = response.json().get("data", {})
            posts = data.get("children", [])

            for post in posts:
                hot_list.append(post.get("data", {}).get("title"))

            next_after = data.get("after")
            if next_after is not None:
                return recurse(subreddit, hot_list, next_after)

            return hot_list
                                                                                                                                
