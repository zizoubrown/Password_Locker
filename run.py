#!/usr/bin/env python3.6
from user import User
from credential import Credential

# USER SECTION

def create_user(fname,lname,password,email):
    '''
    Function to create a new user account
    '''
    new_user = User(fname,lname,password,email)
    return new_user

def save_users(user):
    '''
    Function to save user account
    '''
    user.save_user()

def del_user(user):
    '''
    Fuction to delete a user account
    '''
    user.delete_user()

def find_user(fname):
    '''
    Fution that finds user account by first name and returns the account
    '''
    return User.find_by_first_name(fname)

def display_user():
    '''
    Function that return all the saved user accounts
    '''
    return User.display_users()

# CREDENTIAL SECTION

def create_credential(name,socialMedia,userName,password):
    '''
    Fuction to create a new user credential
    '''
    new_credential = Credential(name,socialMedia,userName,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save user credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function to delete a user credential
    '''
    credential.delete_credential()

def find_credential(userName):
    '''
    Function that finds user credential by username and returns the credential
    '''
    return Credential.find_by_user_name(userName)

def display_credential():
    '''
    Function that return all the save user credetials
    '''
    return Credential.display_credentials()

def main():
    print('Hello! Welcome to PASSWORD LOCKER! What is your name?')
    user_name = input()
    print(f'Hello {user_name}! What would you like to do?')
    print('\n')

    while True:
        print('Use these short codes : cu - create a new user, du - display user, lu - login user, ex - exit Password Locker')
        short_code = input().lower()

        if short_code == 'cu':
            print('New Contact')
            print('-'*20)

            print('First name......')
            f_name = input()

            print('Last name....')
            l_name = input()

            print('Password....')
            pass_word = input()

            print('Email address....')
            email_address = input()

            save_users(create_user(f_name,l_name,pass_word,email_address)) #Create and save new users
            print('\n')
            print(f'New user {f_name} {l_name} created')
            print('\n')

        elif short_code == 'du':

            if display_user():
                print('Here is a list of all your users')
                print('\n')

                for user in display_user():
                    print(f'{user.first_name} {user.last_name} {user.password}')
                
                print('\n')
            
            else:
                print('\n')
                print("You don't seem to have any user account saved yet")
                print('\n')

        elif short_code == 'ex':

            print('Bye......Have a lovely day!!')
            break
            
        elif short_code == 'lu':

            while True:
                print('Use this short codes : cc - create a new user credential, dc - display user credential, ex - exit user credential')
                short_code = input().lower()

                if short_code == 'cc':
                    print('New User Credential')
                    print('-'*15)

                    print('Name......')
                    name = input()

                    print('Social Media.......')
                    social_media = input()

                    print('Username........')
                    user_name = input()

                    print('Password.........')
                    password = input()

                    save_credentials(create_credential(name,social_media,user_name,password)) #creates and saves user credentials
                    print('\n')
                    print(f'New User Credential {name} {social_media} {user_name} {password} created')
                    print('\n')

                elif short_code == 'dc':
                    
                    if display_credential():
                        print('Here is a list of all your User Credentials')
                        print('\n')

                        for credential in display_credential():
                            print(f' {credential.name}, {credential.social_media}, {credential.user_name}, {credential.password}')

                            print('\n')
                        
                        else:
                            print('\n')
                            print('You dont have any User Credentials saved yet!')
                            print('\n')

                elif short_code == 'ex':
                    print('Bye......Hope to see you soon')
                    break

                else:
                    print('I really didnt get that! Please short codes you have been given')

        else:
            print('I really didnt get that. Please use the short codes')

        


if __name__ == '__main__':
    main()