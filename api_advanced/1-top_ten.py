#!/usr/bin/python3
"""
Module that queries Reddit API for top 10 hot posts in a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
                    
    Args:
    subreddit (str): The name of the subreddit to query
                                        
    Returns:
    None: Prints the titles or None if invalid subreddit
                                                        """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
                                                                                
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
            'User-Agent': 'python:reddit.api.project:v1.0 (by /u/your_username)'
            }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
                                                                                                                        
        # Check if we got redirected (invalid subreddit)
        if response.status_code == 302:
            print(None)
            return
                                                                                                                                                                            
        # Check if request was successful
        if response.status_code != 200:
            print(None)                                                                                                                                                                                     return
                                                                                                                                                                                                        data = response.json()
        
        # Check if we have valid data structure
        if 'data' not in data or 'children' not in data['data']:
            print(None)
            return

        posts = data['data']['children']
        
        # Print titles of first 10 posts
    for i, post in enumerate(posts[:10]):
        if 'data' in post and 'title' in post['data']:
            print(post['data']['title'])

    except (requests.exceptions.RequestException, ValueError, KeyError):
        print(None)
