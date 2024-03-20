#!/usr/bin/python3
"""
Script that retrieves and displays the progress of an employee's TODO list
using the JSONPlaceholder API.
"""

import csv
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

    # Write to CSV file
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos_data:
            task_completed_status = 'True' if task.get('completed')\
                                    else 'False'
            formatted_row = [user_id,
                             username,
                             task_completed_status,
                             task.get('title')]
            csv_writer.writerow(formatted_row)

    print(f'Data exported to {csv_filename}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
