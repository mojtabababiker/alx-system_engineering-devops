#!/usr/bin/python3
"""
Python script that, using REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def print_employee_info():
    """
    Print the employee with id=id TODO list
    """
    API_URL = f"https://jsonplaceholder.typicode.com"
    todo_all_employees = dict()

    employees_res = requests.get(f'{API_URL}/users')
    employees_res.raise_for_status()
    employees = employees_res.json()
    for employee in employees:
        # print(f"{employee.get('id', None)}: " + employee.get("name", None))
        id = employee.get("id", None)
        employee_name = employee.get("name", None)
        employee_tasks_info = list()
        if not id:
            continue
        todo_res = requests.get(f'{API_URL}/todos/?userId={id}')
        todo_res.raise_for_status()
        todo_list = todo_res.json()
        total = len(todo_list)

        done_task_res = requests.get(
            f'{API_URL}/todos/?userId={id}&completed=true'
        )
        done_task_res.raise_for_status()
        done_tasks = done_task_res.json()
        done = len(done_tasks)

        for task in todo_list:
            task_info = {"username": employee_name,
                         "task": task.get("title", None),
                         "completed": task.get("completed", None)}
            employee_tasks_info.append(task_info)

        todo_all_employees[f"{id}"] = employee_tasks_info

    with open("todo_all_employees.json", 'w', encoding='utf-8') as json_file:
        json.dump(todo_all_employees, json_file)


if __name__ == "__main__":
    print_employee_info()
