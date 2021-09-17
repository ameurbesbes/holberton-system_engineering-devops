#!/usr/bin/python3
"""
gather data model
"""
import csv
import requests
import sys
import json


if __name__ == '__main__':
    id_user = sys.argv[1]
    name = ""
    total = 0
    done = 0
    arr = []
    data = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            int(id_user))).json()
    name = data["name"]
    username = data.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    for elm in response.json():
        if elm['userId'] == int(id_user):
            total += 1
            if elm['completed'] is True:
                done += 1
                arr.append(elm['title'])
    eq = requests.get(
        'https://jsonplaceholder.typicode.com/users/' +
        (id_user) + '/todos')
    data = {}
    data[id_user] = []
    task = {}
    for x in eq.json():
        task['task'] = x["title"]
        task["completed"] = x["completed"]
        task["username"] = username
        data[id_user].append(task)
    json_object = json.dumps(data, indent=4)
    with open("{}.json".format(id_user), "w") as outfile:
        outfile.write(json_object)
