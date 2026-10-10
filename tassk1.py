tasks = []

while True:
    print("\n===== TO-DO LIST APPLICATION =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter the task: ")

        tasks.append({
            "task": task,
            "completed": False
        })

        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n----- YOUR TASKS -----")

            for i in range(len(tasks)):
                if tasks[i]["completed"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(i + 1, ".", tasks[i]["task"], "-", status)

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to update: "))

            if number >= 1 and number <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[number - 1]["task"] = new_task

                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to delete: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)

                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    # Mark Task as Completed
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i]["task"])

            number = int(input("Enter task number to mark as completed: "))

            if number >= 1 and number <= len(tasks):
                tasks[number - 1]["completed"] = True

                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")
