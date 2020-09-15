#!/usr/bin/python3
""" Calls an API in order to get completed tasks """
import requests
from sys import argv


if __name__ == '__main__':
    try:
        userId = argv[1]
        userData = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".
            format(userId), verify=False).json()
        toDo = requests.get(
            "https://jsonplaceholder.typicode.com/todos?userId={}".
            format(userId), verify=False).json()
        completedTasks = []
        for task in toDo:
            if task.get('completed') is True:
                completedTasks.append(task.get('title'))
        print("Employee {} is done with tasks({}/{}):".
              format(userData.get('name'), len(completedTasks), len(toDo)))
        for task in completedTasks:
            print('\t {}'.format(task))
    except ValueError:
        exit
