#!/usr/bin/python3                                                              
""" return nunmber of subscribers """
import requests as req


def recurse(subreddit):
    """ prints first 10 titles """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {
        'User-Agent': 'unhiredSoftwareDude',
        'From': '824@holbertonschool.com'
    }
    get_posts = req.get(url, headers=headers).json()

    for iter in range(0, 1500):
        hot_post = get_posts['data']['children'][iter]
        if hot_post is None:
            return (0)
        print(hot_post['data']['title'])
