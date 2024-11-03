# -------------------------------- Imports -------------------------------- #
import os
import datetime as dt

# ----------------------------- User-Functions ---------------------------- #


def menu():
    """
    A function that returns the menu options when the username is not
    admin.
    """
    print('Please select from the following options:')
    print('r - register user')
    print('a - add task')
    print('va - view all tasks')
    print('vm - view my tasks')
    print('e - exit')


def alt_menu():
    """
    A function that returns the menu options when the username is
    admin.
    """
    print('Please select from the following options:')
    print('r - register user')
    print('a - add task')
    print('va - view all tasks')
    print('vm - view my tasks')
    print('s - statistics')
    print('e - exit')


def path_directory(filename):
    dirname = os.path.dirname((__file__))
    file_path = os.path.join(dirname, filename)

    return file_path


def read_file(filename):
    """
    A function that takes in a .txt file and reads and returns its
    contents.
    """
    file_path = path_directory(filename)
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        content = file.readlines()

    return content


def user_authentication(filename):
    """
    A function that creates a dictionary of the users and their
    passwords from a .txt file containin the users and their passwords
    on each line
    """
    file_content = read_file(filename)
    user_password_dict = {}
    for element in file_content:
        # Remove any whitespace and unpack values from file line
        username, password = element.strip().split(", ")
        user_password_dict.update({username: password})

    return user_password_dict


def write_file(filename, content):
    """
    A function that opens a filename an adds specified content onto
    what is already on the .txt, or creates a new .txt file if it does
    not exist.
    """
    file_path = path_directory(filename)
    with open(file=file_path, mode="a+", encoding="utf-8") as file:
        file.write(content)


def new_user(filename):
    """
    A function that allows for the admin to register a new user, if the
    user is not on the database already.
    """
    while True:
        print("'Please provide the new username to", end=" ")
        new_username = input("be registered: ").lower()
        if new_username in users.keys():
            print("User is already registered.\n")
        else:
            while True:
                print("Please provide password for,", end=" ")
                new_password = input(f'{new_username.title()}: ')
                password_confirmation = input("Please confirm password: ")
                if new_password == password_confirmation:
                    write_file(filename, f"\n{new_username}, {new_password}")
                    print(f"{new_username} has been added to database.")
                    break
                else:
                    print("\nPassword and confirmation", end=" ")
                    print("password do not match.")
            break


def add_task():
    """
    A  function that stores the inputs of a user about the tasks
    assigned to another authorised user, and returns the input
    information in a readable string format.
    """
    while True:
        taskee = input("Username to assign task to: ")
        # checks using membership operator whether the taskee is in the
        # users list of keys
        if taskee in users.keys():
            break
        else:
            print("User has not been register.", end=" ")
            print("Please assign tasks to registered users only.\n")

    while True:
        print("Provide short description of task", end=" ")
        task_description = input('(<255 characters): ')
        if len(task_description) < 255:
            break
        else:
            print("You have exceeded the limit,", end=" ")
            print("please provide a shorter description", end=" ")
            print("of less than 255 characters\n")

    while True:
        print("Due date of the task in", end=" ")
        due_date = input("dd/mm/yyyy format: ").strip()
        try:
            # Use the date portion of the datetime object
            due_date = dt.datetime.strptime(due_date, '%d/%m/%Y').date()
            break
        except ValueError:
            print("You did not provide the correct format.\n")

    # # Use the date portion of the datetime object
    assignment_date = dt.datetime.today().date()
    task_completion = "No"
    task_title = input("Provide the title of the task: ")
    content_1 = f"\n{taskee}, {task_title}, {task_description}, "
    content_2 = f"{assignment_date}, {due_date}, {task_completion}"
    content = content_1 + content_2

    return content


def view_all(filename):
    """
    A function that splits each line in filename by the comma and
    stores each split into its own variable and stores those variables
    into a readable format, which is returned when the function is
    called
    """
    file_path = path_directory(filename)
    view_all_tasks = ""
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            # Remove any whitespace and unpack values from file line
            line_content = line.strip().split(',')
            (user, task, task_description, date_assigned, due_date,
                task_complete) = line_content
            # Store desired format as the output
            view = (
                f"\n{'-'*182}\n"
                f"\nTask:               {task}"
                f"\nAssigned to:         {user}"
                f"\nDate assigned:      {date_assigned}"
                f"\nDue date:           {due_date}"
                f"\nTask Completed?     {task_complete}"
                f"\nTask description    {task_description}\n"
                f"\n{'-'*182}\n"
            )
            view_all_tasks = view_all_tasks + view
        else:
            pass
    return view_all_tasks


def view_my(filename):
    """
    A function that splits each line in filename by the comma and
    stores each split into its own variable and stores those variables
    into a readable format. If the 'user' variable is the same as the
    username, the other variables related to that 'user' will then be
    stored as a variable which is returned when the function is
    called
    """
    file_path = path_directory(filename)
    view_my_tasks = ""
    with open(file=file_path, mode="r", encoding="utf-8") as file:
        for line in file:
            # Remove any whitespace and unpack values from file line
            line_content = line.strip().split(',')
            (user, task, task_description, date_assigned, due_date,
                task_complete) = line_content
            if user == username:
                # Store desired format as the output
                view = (
                    f"\n{'-'*182}\n"
                    f"\nTask:               {task}"
                    f"\nAssigned to:         {user}"
                    f"\nDate assigned:      {date_assigned}"
                    f"\nDue date:           {due_date}"
                    f"\nTask Completed?     {task_complete}"
                    f"\nTask description    {task_description}\n"
                    f"\n{'-'*182}\n"
                )
                view_my_tasks = view_my_tasks + view
            else:
                pass
    return view_my_tasks


def statistics(user_filename, tasks_filename):
    """
    A function that summerises the total number of users and the total
    number of tasks in the user_filename and tasks_filename, and prints
    the information in a summerised format
    """
    users = user_authentication(user_filename)
    # Counts the current total number of users in the user_filename
    total_users = len(users.keys())
    file_path = path_directory(tasks_filename)
    total_tasks = 0
    with open(file=file_path, mode='r', encoding='utf-8') as file:
        # Use placeholder to iterate file
        for _ in file:
            total_tasks += 1

    print(f"\nTotal number of registered users:\t\t {total_users}")
    print(f"Total number of tasks for all users:\t\t {total_tasks}\n")

# ---------------------------------- Login -------------------------------- #

# store the user/password dictionary as users to be able to access the
# users using the .keys() function, as well as the users passwords,
# using the .values() function


users = user_authentication("user.txt")
while True:
    # Use defensive means to ensure username is stored in lowercaps
    username = input('Please provide username to login: ').lower()
    # Check whether user input, "username" is in our users list
    if username in users.keys():
        print(f"Hello {username}, please provide your")
        password_request = input("password: ")
        # Use .get() function to access the values of the dictionary using
        # key
        if password_request == users.get(username):
            print("Password correct!", end=" ")
            print(f"Welcome back, {username}!\n")
            break
        else:
            print('\nOops, that doesnt seem right,', end=' ')
            print("Let's try that again.")
    else:
        print('Username name on database. Please ensure', end=' ')
        print('you are providing the correct login details\n')

# ---------------------------------- Menu -------------------------------- #
choice = 'x'
while choice != 'e':
    if username == 'admin':
        alt_menu()
    else:
        menu()
    choice = input('')
    if choice == 'r':
        if username == 'admin':
            new_user('user.txt')
            users = user_authentication('user.txt')
        else:
            print('Only admin has the rights to register new users')
    if choice == 'a':
        new_task = add_task()
        write_file('tasks.txt', new_task)
    if choice == 'va':
        all_tasks = view_all('tasks.txt')
        print(all_tasks)
    if choice == 'vm':
        my_tasks = view_my('tasks.txt')
        print(my_tasks)
    if choice == 's':
        statistics('user.txt', 'tasks.txt')
