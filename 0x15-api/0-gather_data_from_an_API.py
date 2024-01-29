#!/usr/bin/python3
"""
Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def print_employee_info(id=""):
    """
    Print the employee with id=id TODO list
    """
    API_URL = f"https://jsonplaceholder.typicode.com/"

    employee_res = requests.get(API_URL + f'users?id={id}')
    employee_res.raise_for_status()

    todo_res = requests.get(API_URL + f'todos/?userId={id}')
    todo_res.raise_for_status()

    done_task_res = requests.get(API_URL +
                                 f'todos/?userId={id}&completed=true'
                                 )
    done_task_res.raise_for_status()

    employee = employee_res.json()[0]
    todo_list = todo_res.json()

    employee_name = employee.get("name", None)

    done_tasks = done_task_res.json()
    done = len(done_tasks)
    total = len(todo_list)

    print(f"Employee {employee_name} is done with tasks({done}/{total})")
    for task in done_tasks:
        print(f'\t {task.get("title", None)}')


if __name__ == "__main__":
    try:
        id = sys.argv[1]
        print_employee_info(id=id)
    except Exception as e:
        pass
