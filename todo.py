import os

def main_menu():
    while True:
        print("Main menu:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete a task")
        print("4. Exit")

        wybor = input("Select the option: ")

        if wybor == '1':
            show_tasks()
        elif wybor == '2':
            menu_add_tasks()
        elif wybor == '3':
            delete_task()
        elif wybor == '4':
            print("Thank you! Goodbye!")
            break
        else:
            print("Incorrect selection. Try again.")

def menu_add_tasks():
    while True:
        print("Select a task category:")
        print("1. Homework")
        print("2. Business tasks")
        print("3. Personal tasks")
        print("4. Health tasks")
        print("5. Educational tasks")
        print("6. Social tasks")
        print("7. Professional tasks")

        category = input("Select the category number: ")

        if category in ('1', '2', '3', '4', '5', '6', '7'):
            add_task(category)
            break
        else:
            print("Incorrect category number. Please try again.")

def show_tasks(category=None):
    category_name = [
        'Homework',
        'Business tasks',
        'Personal tasks',
        'Health tasks',
        'Educational tasks',
        'Social tasks',
        'Professional tasks'
    ]

    if category is not None:
        file_name = f"assignment_{category}.txt"

        try:
            with open(file_name, 'r') as todo:
                assignment = todo.readlines()
                if not assignment:
                    print(f"\n{category_name[int(category) - 1]}: No tasks saved.")
                else:
                    print(f"\n{category_name[int(category) - 1]}:")
                    for idx, exercise in enumerate(assignment, start=1):
                        print(f"{idx}. {exercise.strip()}")
        except FileNotFoundError:
            print(f"\n{category_name[int(category) - 1]}: No tasks saved.")
    else:
        for category in ('1', '2', '3', '4', '5', '6', '7'):
            show_tasks(category)

def delete_task():
    print("Select the category of task to be deleted:")
    for idx, category_name in enumerate([
        'Homework',
        'Business tasks',
        'Personal tasks',
        'Health tasks',
        'Educational tasks',
        'Social tasks',
        'Professional tasks'
    ], start=1):
        print(f"{idx}. {category_name}")

    number_category_to_remove = input("Select the category number: ")

    try:
        number_category_to_remove = int(number_category_to_remove)
    except ValueError:
        print("Incorrect category number.")
        return

    if 1 <= number_category_to_remove <= 7:
        category = str(number_category_to_remove)
        show_tasks(category)
        task_number_to_remove = input("Enter the task number to be deleted: ")

        try:
            task_number_to_remove = int(task_number_to_remove)
        except ValueError:
            print("Incorrect task number.")
            return

        file_name = f"assignment_{category}.txt"

        with open(file_name, 'r') as todo:
            assignment = todo.readlines()

        if 1 <= task_number_to_remove <= len(assignment):
            deleted_task = assignment.pop(task_number_to_remove - 1)

            with open(file_name, 'w') as todo:
                todo.writelines(assignment)

            print(f"Task removed: {deleted_task.strip()}")
        else:
            print("Incorrect job number to be deleted.")
    else:
        print("Incorrect category number to be deleted.")


def add_task(category):
    category_name = [
        'Homework',
        'Business tasks',
        'Personal tasks',
        'Health tasks',
        'Educational tasks',
        'Social tasks',
        'Professional tasks'
    ]

    menu_tasks = {
        '1': menu_homeworks,
        '2': menu_business_tasks,
        '3': menu_personal_tasks,
        '4': menu_health_tasks,
        '5': menu_educational_tasks,
        '6': menu_social_tasks,
        '7': menu_professional_tasks
    }

    while True:
        try:
            print(f"\nAdding a task to a category: {category_name[int(category) - 1]}")
            menu_tasks[category]()

            while True:
                try:
                    whether_to_continue = input("\nDo you wish to add another task? (Y/N): ").upper()
                    if whether_to_continue == 'Y' or whether_to_continue == 'N':
                        break
                    else:
                        raise ValueError("Enter 'Y' or 'N'")
                except ValueError as e:
                    print(f"Error: {e}")
            
            if whether_to_continue == 'N':
                break
        except ValueError as e:
            print(f"Error: {e}")



def menu_homeworks():
    print("Choose a homework assignment:")
    print("1. Cleaning")
    print("2. Washing and ironing")
    print("3. Grocery shopping")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '1')
                save_task(description_task, '1')
                break 
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_business_tasks():
    print("Select a business task:")
    print("1. Project management")
    print("2. Creation of presentations")
    print("3. Data analysis")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '2')  
                save_task(description_task, '2')
                break 
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_personal_tasks():
    print("Select a personal task:")
    print("1. Trip planning")
    print("2. Organisation of events")
    print("3. Budget management")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '3')
                save_task(description_task, '3')
                break 
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_health_tasks():
    print("Select a health task:")
    print("1. Meal planning")
    print("2. Physical exercise")
    print("3. Sleep monitoring")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '4')
                save_task(description_task, '4')
                break 
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_educational_tasks():
    print("Choose an educational task:")
    print("1. Preparation for examinations")
    print("2. Learning planning")
    print("3. Teaching an online lesson")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '5')
                save_task(description_task, '5')
                break  
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_social_tasks():
    print("Choose a social task:")
    print("1. Organisation of social events")
    print("2. Voluntary activities")
    print("3. Neighbourhood assistance")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '6')
                save_task(description_task, '6')
                break 
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")

def menu_professional_tasks():
    print("Choose a professional task:")
    print("1. Report writing")
    print("2. Time management")
    print("3. Scheduling of meetings")
    print("4. Other")

    while True:
        try:
            task_choice = int(input("Select the task number: "))
            if 1 <= task_choice <= 4:
                description_task = download_task_description(str(task_choice), '7')
                save_task(description_task, '7')
                break  
            else:
                print("Incorrect choice. Choose a number between 1 and 4.")
        except ValueError:
            print("Incorrect choice. Choose a number between 1 and 4.")


def download_task_description(task_number, category):
    description_tasks = {
        '1': {
            '1': "Cleaning",
            '2': "Washing and ironing",
            '3': "Grocery shopping",
            '4': "Other"
        },
        '2': {
            '1': "Project management",
            '2': "Creation of presentations",
            '3': "Data analysis",
            '4': "Other"
        },
        '3': {
            '1': "Trip planning",
            '2': "Organisation of events",
            '3': "Budget management",
            '4': "Other"
        },
        '4': {
            '1': "Meal planning",
            '2': "Physical exercise",
            '3': "Sleep monitoring",
            '4': "Other"
        },
        '5': {
            '1': "Preparation for examinations",
            '2': "Learning planning",
            '3': "Teaching an online lesson",
            '4': "Other"
        },
        '6': {
            '1': "Organisation of social events",
            '2': "Voluntary activities",
            '3': "Neighbourhood assistance",
            '4': "Other"
        },
        '7': {
            '1': "Report writing",
            '2': "Time management",
            '3': "Scheduling of meetings",
            '4': "Other"
        }
    }

    return description_tasks.get(category, {}).get(task_number, "No description")


def save_task(description_task, category):
    with open(f"assignment_{category}.txt", 'a') as todo:
        todo.write(description_task + '\n')

if __name__ == "__main__":
    main_menu()
