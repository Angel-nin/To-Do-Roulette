import random
from datetime import datetime

# [task_name, done_status, deadline]

categories = {
    1: {"name": "School Work", "tasks": []},
    2: {"name": "House Chores", "tasks": []},
    3: {"name": "Self-care", "tasks": []},
    4: {"name": "Errands", "tasks": []},
    5: {"name": "Bucket List", "tasks": []}
}

# dates 

def get_today():        #Get the date today
    return datetime.today().date()  #.today (get the date today w time);    .date (gets rid of thee time)


def get_status(deadline, done):      #get the status (if pending, done or overdue)
    today = get_today()

    if done:
        return "Done"

    if deadline < today:
        days = (today - deadline).days
        return f" Overdue by {days} day(s)"
    else:
        return " Pending"


#  DISPLAY 

def show_main_menu():     
    print("\n" + "="*40)      #display 40 "="
    print("TO-DO ROULETTE")
    print("1. Categories")
    print("2. Progress")
    print("3. Exit")


def show_categories():
    print("\n" + "="*40)
    print("CATEGORIES")
    for num, data in categories.items():    #checks the content if the dictionary categories
        print(f"{num}. {data['name']}")     #displays the Categories w numbers


def show_tasks(cat_num):    #cat_num = category number    
    tasks = categories[cat_num]["tasks"]    #checks the list of tasks inside a category
    print("\nTasks in", categories[cat_num]["name"])    #displays tasks inside a category (cat_num = catgory )

    if not tasks:
        print("(no tasks yet)")
        return

    for i, (name, done, deadline) in enumerate(tasks, 1):   #enumerate coounts the items starting at 1
        status = get_status(deadline, done)     #gets the status of the current task being checked
        print (f"{i}. {name} | Due: {deadline} | {status}")   #prints th task w the u know u know


# CATEGORY MENU 

def category_menu(cat_num):
    while True:
        print("\n" + "-"*40)
        print(categories[cat_num]["name"])  #display catgeory name
        print("1. Add task")
        print("2. Pick random task")
        print("3. Mark task done")
        print("4. Show tasks")
        print("5. Exit category")

        choice = input("Enter choice: ")

        
        if choice == "1":   # ADD TASK
            name = input("Enter task: ").strip()    #.strip cleaning accidental spaces
            date_str = input("Enter deadline (YYYY-MM-DD): ").strip()

            try:    #tries this part of the code
                deadline = datetime.strptime(date_str, "%Y-%m-%d").date()   #converts the date to real date (.strptime reads str as date)
                categories[cat_num]["tasks"].append([name, False, deadline])    #adds the task to the category
                print("Task added.")
            except: #if smth happens in the try section it will jump here
                print("Invalid date format.")

        # RANDOM TASK (ONLY NOT DONE)
        elif choice == "2":
            tasks = [t for t in categories[cat_num]["tasks"] if not t[1]]   #filters unfinished tasks

            if tasks:
                name, done, deadline = random.choice(tasks) #picks a random task
                print(f"  You got: {name} (Due: {deadline})")
            else:
                print("No pending tasks available.")

        # MARK DONE
        elif choice == "3":
            tasks = categories[cat_num]["tasks"]

            if not tasks:   #if no tasks
                print("No tasks.")
                continue

            show_tasks(cat_num)

            try:
                num = int(input("Task number: "))
                tasks[num-1][1] = True  #changes from false to true so then it will print 
                print("Marked as done.")
            except:
                print("Invalid input.")

        # SHOW TASKS
        elif choice == "4":
            show_tasks(cat_num)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


#  PROGRESS 

def show_progress():
    print("\n" + "="*40)
    print("COMPLETED TASKS")

    found = False

    for data in categories.values():    #checks all catgories
        done_tasks = [t for t in data["tasks"] if t[1]] #filters completed tasks only and adds it to done_task

        if done_tasks:
            found = True    
            print("\n" + data["name"] + ":")
            for name, done, deadline in done_tasks:
                print(f" {name} (Due: {deadline})")

    if not found:
        print("No completed tasks yet.")


#  MAIN LOOP 

while True:
    show_main_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        show_categories()
        try:
            c = int(input("Enter category number: "))
            if c == 6:  #back
                continue
            if c in categories: #opens the category w the number (c)
                category_menu(c)
            else:
                print("Invalid category.")
        except:
            print("Enter a number.")

    elif choice == "2":
        show_progress()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
