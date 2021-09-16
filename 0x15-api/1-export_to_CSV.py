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
        with open('{}.csv'.format(id_user), 'w') as csvfile:
            spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for x in arr:
                spamwriter.writerow([id_user, name, x])
