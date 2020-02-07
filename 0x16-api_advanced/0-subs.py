#!/usr/bin/python3
""" script returns amount of subscribers of given subreddit """

import requests as req



def number_of_subscribers(subreddit):
    """ gets number of subs to subreddit """
    url = "https://api.reddit.com/r/{}/about".format(
        subreddit)
    headers = {
        'User-Agent': 'macOS:macbook.pro: by (unhiredSoftwareDude)',
        'From': '824@holbertonschool.com'
    }
    grab_content = req.get(url, headers=headers).json()

    if 'subscribers' in grab_content['data']:
        subscribers = grab_content['data']['subscribers']
        return(subscribers)
    else:
        return(0)
