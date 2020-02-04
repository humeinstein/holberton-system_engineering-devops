#!/usr/bin/python3
import json
import requests as req


if __name__ == "__main__":
    enddict = {}
    newlist = []
    userreq = req.get("https://jsonplaceholder.typicode.com/users").json()
    taskreq = req.get("https://jsonplaceholder.typicode.com/todos").json()
    newdict = {}
    for person in userreq:
        for task in taskreq:
            if person["id"] == task["userId"]:
                newdict["task"] = task["title"]
                newdict["completed"] = task["completed"]
                newdict["username"] = person["username"]
                newlist.append(newdict)
        enddict[person["id"]] = newlist

    with open("todo_all_employees.json", 'w') as f:
        json.dump(enddict, f)
