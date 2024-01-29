#!/usr/bin/python3
"""
Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def print_employee_info():
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

    with open(f"{id}.csv", 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, doublequote=True,
                                quoting=csv.QUOTE_ALL)
        for task in todo_list:
            csv_writer.writerow([f'{id}', employee_name,
                                 task.get("completed", None),
                                 task.get("title", None)])


if __name__ == "__main__":
    id = sys.argv[1]
    print_employee_info(id=id)
