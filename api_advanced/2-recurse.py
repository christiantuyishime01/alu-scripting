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
            header = {'User-Agent': 'CustomUserAgent/1.0'}
            param = {'limit': 100, 'after': after}
            response = requests.get(url, headers=header, params=param)

            if response.status_code != 200:
                return None
            else:
                json_res = response.json()
                after = json_res.get('data').get('after')
                has_next = \
                        json_res.get('data').get('after') is not None
                hot_articles = json_res.get('data').get('children')
                [hot_list.append(article.get('data').get('title'))
                    for article in hot_articles]
                
                return recurse(subreddit, hot_list, after=after) \
                    if has_next else hot-list
                                                                                                                                
