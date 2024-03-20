#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an employee's TODO list
using the JSONPlaceholder API.
"""

import json
import requests
import sys


def export_all_employees_to_json():
    """
    Fetches and exports TODO list progress for all employees in JSON format.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch all users
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()

    # Create a dictionary to store tasks for each user
    all_tasks = {}

    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch user's TODO list
        todos_response = requests.get(f'{base_url}/todos?userId={user_id}')
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

        all_tasks[str(user_id)] = task_list

    # Write to JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    export_all_employees_to_json()
