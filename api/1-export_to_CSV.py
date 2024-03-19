#!/usr/bin/python3
"""
This script fetches data from a REST API and exports it in CSV format.
"""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches user and TODO data from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing user data and TODO data.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todo_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        if 'id' not in user_data:
            print("Employee not found.")
            return

        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()
        return user_data, todo_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


def export_to_csv(employee_id, user_data, todo_data):
    """
    Exports the employee's TODO list data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        user_data (dict): User data.
        todo_data (list): List of TODO items.
    """
    user_id = user_data.get('id')
    username = user_data.get('username')
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for task in todo_data:
            task_id = task.get('id')
            task_title = task.get('title')
            completed = task.get('completed')
            writer.writerow([user_id, username, completed, task_title])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_employee_data(employee_id)
    if user_data and todo_data:
        export_to_csv(employee_id, user_data, todo_data)
