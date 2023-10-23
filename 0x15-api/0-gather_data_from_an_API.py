#!/usr/bin/python3
"""Task 0"""
import requests
import sys

def fetch_employee_data(employee_id):
    """function to fetch data"""
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    tasks_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    completed_tasks = [task for task in tasks_data if task['completed']]
    total_tasks = len(tasks_data)

    print(f"Employee {employee_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_data(employee_id)
