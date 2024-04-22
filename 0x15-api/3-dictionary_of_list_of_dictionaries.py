#!/usr/bin/python3
""" a script that, using this REST API, for a given employee ID, """

import json
import requests
import sys


if __name__ == "__main__":

    all_data = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    data = {}

    for user in all_data:
        ID = user.get('id')
        all_data = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                ID)).json()
        setof_data = []
        data[ID] = setof_data

        for task in all_data:
            setof_data.append({
                "task":
                    task.get('title'),
                    "completed":
                    task.get('completed'),
                    "username":
                    user.get('username')
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f)
