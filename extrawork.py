#This Program is essentially just tracking work of the user


project_running = True #this is for option 4 in case the user wants to quit the program.
tasks = [] #this is mainly for option 2, to view the tasks that have been added. It is a list that will store the tasks as strings



#THE FOLLOWING FUNCTIONS ARE FOR THE OPTIONS THAT THE USER CAN CHOOSE FROM IN THE MAIN LOOP
def add_task():
    task_name = input("Enter the name of the task: ")
    tasks.append(task_name)
    print(f"Task '{task_name}' added.")

def view_tasks():
    if len(tasks) == 0: #if the length of the list is 0, then there are no tasks to show
        print("No tasks to show.")
    else:
        print("Tasks to do:")
        for index, task in enumerate(tasks, start=1): #index, task are basically variables that are used to store the index and the task in the list. enumerate is a function that allows you to loop through a list and get the index and the value at the same time. start=1 means that the index will start at 1 instead of 0    
            print(f"{index}. {task}") #this prints the index and the task in a formatted way, the f before the string allows for a variable to be put into the string

def check_off_task():
    if len(tasks) == 0:
        print("No tasks to check off.")
    else:
        view_tasks()
        task_number = int(input("Enter the number of the task to check off: "))
        if 1 <= task_number <= len(tasks):
            checked_task = tasks.pop(task_number - 1) #pop() removes the task and then returns it back, so we can store it in a variable to print it out later
            print(f"Task '{checked_task}' checked off.")
        else:
            print("Invalid task number.")



#Main project loop, this is where the user will choose what they want to do. The loop will continue until the user chooses to quit the program.
while project_running == True:
    print("=========== Homework Tracker ===========")
    print("Choose an Option by entering a number")
    print("1.   Add a task")
    print("2.   View Tasks to do")
    print("3.   Check off a task")
    print("4.   Quit Program")
    user_input = int(input("Which option do you choose: "))

#user inputs that run the functions based on the number they chose.
    if user_input == 1:
        # adds a task
        add_task()
    elif user_input == 2:
        # views tasks
        view_tasks()
    elif user_input == 3:
        # check off a task
        check_off_task()
    elif user_input == 4:
        print("Quitting Program")
        print("Goodbye")
        project_running = False
    else: #this is in case the user inputs a number that isn't 1, 2, 3, or 4.
        print("Invalid option") 
        print("Please choose a number between 1 and 4")