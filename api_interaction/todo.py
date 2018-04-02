import requests
import socket
from pprint import pformat

def get_todos():
    request = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = []
    for todo in request.json():
        todos.append(pformat(todo))
    return '\n'.join(todos)

def delete_todo():
    print('enter the id of the todo you would like to delete: ')
    id = input()
    request = requests.delete('https://jsonplaceholder.typicode.com/todos/{}'.format(id))
    return request.status_code

def create_todo():
    print('enter a title: ')
    title = input()
    print('enter a user id: ')
    userid = input()
    print('enter "true" if complete')
    completed = input() 

    body = {
        'userId': userid,
        'title': title,
        'completed': "true" if completed == "true" else "false"
    }

    request = requests.post('https://jsonplaceholder.typicode.com/todos', data=body)
    return pformat(request.json())


def control_loop():
    greeting = 'press c to create\npress d to delete\npress g to get\npress q to quit\n'
    option = ''
    funcs = {
        'c': create_todo,
        'd': delete_todo,
        'g': get_todos
    }

    while option != 'q':
        print(greeting)
        option = input().lower()
        if option in funcs:
            try:
                output = funcs[option]()
                print(output)
            except requests.exceptions.ConnectionError:
                print('Looks like you are not connected to the internet. Try connecting.')


if __name__ == '__main__':
    control_loop()
