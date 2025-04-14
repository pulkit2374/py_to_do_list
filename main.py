print("Welcome to PyToDo! ")

tasks = []
while True:
    print("Choose an option: \n 1. Add Task \n 2. View Task \n 3. Remove Task \n 4. Exit")
    opt = int(input())
    if opt == 1:
        inp = input("Enter the task: ")
        tasks.append(inp)
        print("Task added successfully")

    elif opt == 2:
        print("Your tasks: ")
        print(tasks)

    elif opt == 3:
        inp = input("Enter the task to remove: ").lower()
        for task in tasks:
            if task.lower() == inp:
                tasks.remove(task)
                print("Task removed")
            else:
                print("Task not found")

    elif opt == 4:
        print("See you next time!")
        break
    
    else:
        print("Invalid option, try again...")
