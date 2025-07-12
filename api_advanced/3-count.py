#!/usr/bin/python3
"""
Recursively counts and prints sorted keyword occurrences in hot post titles
from a given subreddit.
"""

import requests
import re


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Queries Reddit API recursively, counts occurrences of keywords,
    and prints them in sorted order (by count desc, then alphabetically).
    """
    if not counts:
        for word in word_list:
            key = word.lower()
            counts[key] = counts.get(key, 0)

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom-user-agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        words = re.findall(r'\b\w+\b', title)
        for word in counts:
            counts[word] += words.count(word)
    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    filtered = {k: v for k, v in counts.items() if v > 0}
    if not filtered:
        return

    sorted_counts = sorted(filtered.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
                                                                                                                                                                                                        
