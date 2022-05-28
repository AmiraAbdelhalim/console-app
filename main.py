
# lab2 console app

# imports
from models.user import create_user, find_user
from helpers.validators import validate_email, validate_mobile, confirm_user_password
from models.project import create_project, get_all_projects, get_project_by_title, delete_project

while True:
    print('> Welcome to Crowd-Funding console')
    print('> New User Registration - press(1)')
    print('> Login - press(2)')
    print('> Exit- press(3)')

    user_choice = int(input('> Your Choice '))
    # registration
    if user_choice == 1:
        while True:
            print('Enter Your Data')
            first_name = input('> Firstname: ')
            last_name = input('> Lastname: ')
            email = input('> Email: ')
            if not validate_email(email):
                print('Please, enter a valid email.')
                continue
            password = input('> Password: ')
            confirm_password = input('> Confirm Password: ')
            if not confirm_user_password(password, confirm_password):
                print('password mismatch')
                continue
            mobile_phone = input('> Mobile Number: ')
            if not validate_mobile(mobile_phone):
                print('Please, enter valid mobile number')
            created = create_user(first_name, last_name, email, password, confirm_password, mobile_phone)
            if created:
                print('> Congratulations')
            else:
                print('User is not created')
            break
    # login
    elif user_choice == 2:
        print('Enter Login Data')
        email = input('> Email: ')
        password = input('> Password: ')
        user = find_user(email, password)
        print('user => ', user)
        if user:
            user_id = user[0]
            while True:
                print(f'> Hello, {user[1]}')
                print('> Create Project - press (0)')
                print('> View Projects - press (1)')
                print('> View One Project - press (2)')
                print('> Delete project - press (3)')
                print('> Exit - press (4)')
                auth_user_choice = int(input('> Your choice '))
                # create project
                if auth_user_choice == 0:
                    title = input('> Project Tile: ')
                    details = input('> Project Details: ')
                    total = input('> Project Total: ')
                    start_date = input('> Project Start Date: ')
                    end_date = input('> Project End Date: ')
                    created = create_project(user_id, title, details, total, start_date, end_date)
                    if created:
                        print('Project Created')
                    else:
                        print('project is not created')
                    break
                # view projects
                elif auth_user_choice == 1:
                    print('> All Projects')
                    projects = get_all_projects()
                    if not len(projects):
                        print("There's no projects")
                    elif len(projects):
                        count = 0
                        for project in projects:
                            count += 1
                            print(f'{count}) project title {project[2]} | project details {project[3]} | project target {project[4]} | project start date {project[5]} | project end date {project[6]}')
                    else:
                        print('something went wrong')
                # view one project
                elif auth_user_choice == 2:
                    title = input('> Enter title of the desired project: ')
                    project = get_project_by_title(title)
                    if project:
                        print(f' project title {project[0]} | project details {project[1]} | project target {project[2]} | project start date {project[3]} | project end date {project[4]}')
                    else:
                        print('something went wrong')
                # delete project
                elif auth_user_choice == 3:
                    title = input('> Enter Project Title: ')
                    print('deleting project ...')
                    deleted = delete_project(user_id, title)
                    if deleted:
                        print('Project deleted successfully')
                    else:
                        print('project is not deleted')
                # exit
                elif auth_user_choice == 4:
                    print('goodbye!')
                    break
    # exit
    elif user_choice == 3:
        print('goodbye!')
        break
    else:
        print('Sorry, Unknown Input')


