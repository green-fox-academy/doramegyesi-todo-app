import sys
print(sys.argv)

text = open("todo_app.txt", "r")
todo_list = text.readlines()
text.close()

def print_help():
    help_info =    ["Python todo application",
                    "=======================",
                    "Command line arguments:",
                    "-l Lists all the tasks",
                    "-a Adds a new task",
                    "-r Removes a task",
                    "-c Completes task"]

    for content in help_info:
        print(content)

def print_todo_list():
    if len(todo_list) == 0:
        print("No todos for today, man!")
    else:
        for todo in range(1, len(todo_list) + 1):
            print(str(todo) + " [ ] " + (todo_list[todo - 1]))

def controller():
    if len(sys.argv) >= 2:
        if sys.argv[1] == "-l":
            print_todo_list()
        if sys.argv[1] == "-a":
            add_new_task()
        if sys.argv[1] == "-r":
            remove_task()
        if sys.argv[1] == "-c":
            complete_task()
    else:
        print_help() 

def add_new_task():
    if len(sys.argv) > 2:
        new_todo = open("todo_app.txt", "a")
        new = sys.argv[2] + "\n"
        add_todo = new_todo.writelines(new)
        new_todo.close()
    else:
        print("no new task added")

def remove_task():
    if len(sys.argv) > 2:
        removing = open("todo_app.txt")

controller()
