#!/usr/bin/python3
""" export as json """


if __name__ == "__main__":
    import json
    import requests as req
    import sys

    todorequest = req.get("https://jsonplaceholder.typicode.com/todos",
                          params={"userId": int(sys.argv[1])})
    listcontent = todorequest.json()
    usersrequest = req.get("https://jsonplaceholder.typicode.com/users/{}".format
                           (sys.argv[1])).json()

    jsonlist = []
    for change in req.get("https://jsonplaceholder.typicode.com/todos").json():
        if usersrequest["id"] == change["userId"]:
            newcontent = {}
            newcontent["task"] = change["title"]
            newcontent["completed"] = change["completed"]
            newcontent["username"] = ["username"]
            jsonlist.append(newcontent)

    jsond = {str(sys.argv[1]): listcontent}

    with open('{}.json'.format(sys.argv[1]), 'w') as jsonf:
        json.dump(jsond, jsonf)
