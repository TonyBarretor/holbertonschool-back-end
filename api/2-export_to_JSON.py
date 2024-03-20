#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an employee's TODO list
using the JSONPlaceholder API.
"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the employee's TODO list progress.

    Parameters:
        employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f'{base_url}/users/{employee_id}')
    user_data = user_response.json()
    user_id = user_data.get('id')
    username = user_data.get('username')

    # Fetch user's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Create JSON data format
    task_list = []
    for task in todos_data:
        task_title = task.get('title')
        task_status = task.get('completed')
        task_dict = {"task": task_title,
                     "completed": task_status,
                     "username": username}
        task_list.append(task_dict)

    json_data = {str(user_id): task_list}

    # Write to JSON file
    json_filename = f'{user_id}.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)

    print(f'Data exported to {json_filename}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
