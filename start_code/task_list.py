tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def print_uncompleted_tasks( list ):
    uncompleted_tasks = None
    for task in list:
        if task["completed"] == False:
            uncompleted_tasks = task["description"]
            print(uncompleted_tasks)
    if uncompleted_tasks == None:
        return print(uncompleted_tasks)

# print_uncompleted_tasks(tasks)

def print_completed_tasks( list ):
    completed_tasks = None
    for task in list:
        if task["completed"] == True:
            completed_tasks = task["description"]
            print(completed_tasks)

    if completed_tasks == None:
        return print(completed_tasks)

# print_completed_tasks(tasks)

def print_all_tasks( list ):
    for task in list:
        print(task["description"])

# print_all_tasks(tasks)

def print_tasks_per_time_taken( list, time_taken ):
    tasks = None
    for task in list:
        if task["time_taken"] >= time_taken:
            tasks = task["description"]
            time = task["time_taken"]
            print(f"{tasks} takes {time} minutes")

    if tasks == None:
        return print("No task takes this amount of time")

# print_tasks_per_time_taken(tasks, 61)

def print_task_by_description( list, description):
    for task in list:
        if task["description"].lower() == description.lower():
            return print(task)

    return print("No task exists with that description")

# print(print_task_by_description(tasks, "Walk Dog"))

def update_task_as_complete( list, description ):
    for task in list:
        if task["description"].lower() == description.lower():
            task["completed"] = True 
            return print(f"{description} has been updated to completed!")
    return print("No such task exists!")

# update_task_as_complete(tasks, "clean windows")
# print(tasks[1])

def add_task( list, description, completed, time_taken):
    list.append({"description": description, "completed": completed, "time_taken": time_taken})
    return print(f"{list[-1]} is added!")

# add_task( tasks, "Hoover", False, 15)


select = None

while select == None:
    print("-------------------")
    print("Menu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
    select = input("Select an option: ")
    print("-------------------")

    if select == "1":
        print_all_tasks(tasks)
        select = None
    elif select == "2":
        print_uncompleted_tasks(tasks)
        select = None
    elif select == "3":
        print_completed_tasks(tasks)
        select = None
    elif select == "4":
        task = input("Enter task to be completed: ")
        update_task_as_complete(tasks, task)
        select = None
    elif select == "5":
        time = input("Enter a time: ")
        print_tasks_per_time_taken(tasks, int(time))
        select = None
    elif select == "6":
        description = input("Enter a task description: ")
        print_task_by_description(tasks, description)
        select = None
    elif select == "7":
        description = input("Enter task's description: ")
        completed = input("Enter if task complete (True or False): ")
        time_taken = input("Enter time to do task: ")
        add_task( tasks, description, bool(completed), int(time_taken))
        select = None
    elif select.lower() == "m":
        select = None
    else:
        break