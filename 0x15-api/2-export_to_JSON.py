#!/usr/bin/python3
"""
gather data model
"""
import json
import requests
import sys


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
    with open("{}.json".format(id_user), "w") as outfile:
        json.dump({id_user: [{"title": x.get("title"), "completed": x.get(
            "completed"), "username": username}for x in eq.json()]}, outfile)
