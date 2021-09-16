#!/usr/bin/python3
"""
gather data model
"""
import requests
import sys
import csv


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
    with open("{}.csv".format(sys.argv[1]), "w") as file_c:
        writer = csv.writer(file_c, quoting=csv.QUOTE_ALL)
        for task in eq.json():
            writer.writerow([id_user, name,
                            task.get("completed"), task.get("title")])
