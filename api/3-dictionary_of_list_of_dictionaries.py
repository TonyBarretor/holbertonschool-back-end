#!/usr/bin/python3
"""
This script retrieves tasks from a REST API and exports them to a JSON file.
"""

import json
import requests

def main():
    """
    Main function to retrieve tasks and export them to a JSON file.
    """
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url).json()
    tasks = requests.get(url).json()

    all_tasks = {}

    for user in users:
        user_tasks = []
        for task in tasks:
            if task.get('userId') == user.get('id'):
                task_data = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                user_tasks.append(task_data)
        all_tasks[str(user.get('id'))] = user_tasks

    with open('todo_all_employees.json', 'w') as file:
        json.dump(all_tasks, file)

if __name__ == "__main__":
    main()
