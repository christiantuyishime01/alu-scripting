#!/usr/bin/python3
"""
Module for querying Reddit API to get top 10 hot posts from a subreddit.
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
        print("None")
        return
                                                                                    
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
                                                                                                
    # Custom User-Agent to avoid rate limiting
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
            }
                                                                                                                        
    # Parameters to limit results and avoid redirects
    params = {
            'limit': 10
            }
                                                                                                                                                
    try:
        # Make request without following redirects
        response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

        # Check if we got a redirect (invalid subreddit)
        if response.status_code == 302:
            print("None")
            return
        
        # Check if request was successful
        if response.status_code != 200:
            print("None")
            return
        
        # Parse JSON response
        data = response.json()
                                                                                                                                                                                                        # Check if we have the expected structure
                                                                                                                                                                                                        if 'data' not in data or 'children' not in data['data']:
                                                                                                                                                                                                            print("None")
                                                                                                                                                                                                            return
        
        # Extract and print post title
        posts = data['data']['children']
        
        # If no posts found, subreddit might be invalid
        
        if not posts:
            print("None")
            return
        
        # Print titles of first 10 posts
        for post in posts[:10]:
            if 'data' in post and 'title' in post['data']:
                print(post['data']['title'])

    except (requests.RequestException, ValueError, KeyError:
            print("None")
