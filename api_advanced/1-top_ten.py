#!/usr/bin/python3
"""Script that fetch all hot post for a given subreddit with recursive call."""

import requests

headers = {'User-Agent': 'MyAPI/0.0.1'}


def recurse(subreddit, after="", hot_list=[], page_counter=0):
    """Return all hot posts in a subreddit."""

    subreddit_url = "https://reddit.com/r/{}/hot.json".format(subreddit)

    parameters = {'limit': 100, 'after': after}
    response = requests.get(subreddit_url, headers=headers, params=parameters)

    if response.status_code == 200:
        json_data = response.json()
            

    for child in json_data.get('data').get('children'):
        title = child.get('data').get('title')
        hot_list.append(title)

                                                                
    after = json_data.get('data').get('after')
    if after is not None:
        page_counter += 1
        return recurse(subreddit, after=after,
                hot_list=hot_list, page_counter=page_counter)
    else:
        return hot_list

    else:
        return None

if __name__ == '__main__':
    print(recurse("zerowastecz"))
