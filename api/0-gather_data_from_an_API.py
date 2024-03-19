import requests
import sys

def fetch_employee_data(employee_id):
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

def display_todo_progress(employee_id, user_data, todo_data):
    employee_name = user_data['name']
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todo_data = fetch_employee_data(employee_id)
    if user_data and todo_data:
        display_todo_progress(employee_id, user_data, todo_data)
