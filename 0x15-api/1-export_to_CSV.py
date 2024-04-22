#!/usr/bin/python3

""" n script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress. """

import csv
import requests
import sys


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    ID = sys.argv[1]
    user_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(ID)).json().get(
            'username')
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            ID)).json()
    todos_done = [todo for todo in todos if todo.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, len(todos_done), len(todos)))

    with open('{}.csv'.format(ID), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([ID, user_name, todo.get('completed'),
                             todo.get('title')])
