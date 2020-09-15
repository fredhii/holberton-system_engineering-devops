#!/usr/bin/python3
""" Calls an API in order to get completed tasks """
import requests
import urllib3
from sys import argv
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == '__main__':
    userId = argv[1]
    userData = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                            format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(userData.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
