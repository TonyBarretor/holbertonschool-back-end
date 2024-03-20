#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an employee's TODO list
using the JSONPlaceholder API.
"""

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
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todos_response = requests.get(f'{base_url}/todos?userId={employee_id}')
    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    num_done_tasks = len(done_tasks)

    # Display info
    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, num_done_tasks, total_tasks))
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
