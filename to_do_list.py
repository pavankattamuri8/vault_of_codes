def display_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.")

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid task index. Please enter a valid task index.")

def main():
    todo_list = []

    print("Welcome to your To-Do List!")

    while True:
        print("\nOptions:")
        print("1. Display Your To-Do List")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            task = input("Enter the task you want to add: ")
            add_task(todo_list, task)
        elif choice == "3":
            try:
                task_index = int(input("Enter the task index you want to remove: "))
                remove_task(todo_list, task_index)
            except ValueError:
                print("Please enter a valid task index (a number).")
        elif choice == "4":
            print("Thank you for using your To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()