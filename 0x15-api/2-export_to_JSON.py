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
    API_URL = "https://jsonplaceholder.typicode.com"

    employee_res = requests.get(f'{API_URL}/users?id={id}')
    employee_res.raise_for_status()

    todo_res = requests.get(f'{API_URL}/todos/?userId={id}')
    todo_res.raise_for_status()

    done_task_res = requests.get(
        f'{API_URL}/todos/?userId={id}&completed=true'
    )
    done_task_res.raise_for_status()

    employee = employee_res.json()[0]
    todo_list = todo_res.json()

    employee_name = employee.get("name", None)

    done_tasks = done_task_res.json()
    done = len(done_tasks)
    total = len(todo_list)

    tasks_info = list()
    for task in todo_list:
        task_info = {"task": f"{task.get('title', None)}",
                     "completed": f"{task.get('completed', None)}",
                     "username": employee_name}
        tasks_info.append(task_info)

    with open(f"{id}.json", 'w', encoding='utf-8') as json_file:
        json.dump({f"{id}": tasks_info}, json_file)


if __name__ == "__main__":
    try:
        id = sys.argv[1]
        print_employee_info(id=id)
    except Exception as e:
        pass
