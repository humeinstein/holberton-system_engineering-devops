#!/usr/bin/python3                                                                                     
""" return info on employees """

if __name__ == "__main__":
    import csv
    import json
    import requests as req
    import sys

    todorequest = req.get("https://jsonplaceholder.typicode.com/todos",
                     params={"userId": int(sys.argv[1])})
    userstodocontent = todorequest.json()
    userrequest = req.get("https://jsonplaceholder.typicode.com/users",
                          params={"id": int(sys.argv[1])})
    
    userinfo = userrequest.json()
    username = userinfo[0].get("username")
    
    for change in userstodocontent:
        change["username"] = username
        change.pop("id")

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=["userId", "username", "completed", "title"],
                                quoting=csv.QUOTE_ALL)
        for row in userstodocontent:
            writer.writerow(row)
    
    
