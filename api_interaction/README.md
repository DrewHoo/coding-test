## Run the code
Note: This code was developed with Python 3.6 on Mac OS
0) Follow the instructions in the README at the root of the project
1) Type `python api_interaction/todo.py` into the shell

## Notes
If I had more time, I'd write some tests and better status code handling logic. For instance, if you try to delete a todo with an id > 200, you get a 404, and it'd be nice to tell the user 'todo not found' rather than '404'.