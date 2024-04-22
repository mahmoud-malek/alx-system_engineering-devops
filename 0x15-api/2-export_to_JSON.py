#!/usr/bin/python3
""" a script that, using this REST API, for a given employee ID, """

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    ID = sys.argv[1]
    all_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            ID)).json()

    setof_data = []
    data = {ID: setof_data}

    for task in all_data:
        setof_data.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(ID)).json().get('username')})

    with open('{}.json'.format(ID), 'w') as f:
        json.dump(data, f)
