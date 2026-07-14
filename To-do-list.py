tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if tasks:
            print("Your Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks yet!")

    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.") 