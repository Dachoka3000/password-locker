#!/usr/bin/env python3.8
from user import User
from credentials import Credentials
import random
import string



def create_user(username, email, password):
    '''
    function to create a new user account
    '''

    new_user = User(username, email, password)
    return new_user

def save_user(user):
    '''
    function to save a user
    '''

    User.save_user(user)

def find_user(username):
    '''
    function to find a user by the user name
    '''

    return User.find_by_username(username)

def check_existing_user(username):
    '''
    function that finds a user by their username and returns boolean if they exist
    '''

    return User.user_exist(username)

def create_credential(account,user_name, pass_word):
    '''
    function to create a new credential account
    '''

    new_credential = Credentials(account, user_name, pass_word )
    return new_credential

def save_credential(credentials):
    '''
    function to save credential
    '''

    credentials.save_credentials()

def del_credential(credentials):
    '''
    function to delete a credential
    '''

    credentials.delete_credentials()

def find_credential(account):
    '''
    function to find credentials usinfg the account name
    '''

    return Credentials.find_by_account(account)

def check_existing_credential(account):
    '''
    functions that checks if a credential exists and returns a boolean
    '''

    return Credentials.credentials_exist(account)

def display_credentials():
    '''
    function that returns all the saved credentials
    '''

    return Credentials.display_credentials()

def get_password(length):
    '''
    functions that generates a new password from random letters
    '''

    letters = string.ascii_letters
    pass_generated = ''.join(random.choice(letters) for i in range(length))
    return pass_generated

def copy_credential(account):
    '''
    function that copy-pastes to clipboard the username that matches the accountname
    '''

    return Credentials.copy_details(account)




def main():
    print("Hello. Welcome to password locker.")
    
    while True:
        print("What would you like to do?\n Click \n s to sign up \n l to log in \n x to exit")
        option_chosen = input()

        if option_chosen == 's':
            print("Sign up for a new account")
            print("Enter username:....")
            username = input()

            print("Enter email:...")
            email = input()

            print("Enter a password:...")
            password = input()

            save_user(create_user(username, email, password))
            print('\n')
            print("-"*80)
            print(f'Account for {username} has been created. Log in to continue')
            print("-"*80)
            print("\n")
            

        elif option_chosen == 'l':
            print("Enter your username:...")
            username = input()
            print("Enter your email")
            email = input()
            print("Enter your password:...")
            password = input()

            old_user = check_existing_user(username)

            if old_user:
                current_user = find_user(username)
                print('\n')
                print(f"hey {username}, you are now logged in")
                print("-"*50)

                while True:
                    print("What would you like to do? Use these short codes to navigate:\n cc- Create a credential account for any app\n dl- delete a saved credential\n vw- view your saved credentials\n x- exit ")
                    short_code = input().lower()

                    if short_code == 'cc':
                        print("Create new credential account")
                        print("-"*50)

                        print("Enter name of account/ app:...")
                        account = input()

                        print("Enter your username for that account/ app:...")
                        user_name = input()

                        print("Would you like us to generate a password for you?\n Click:\n y- for yes\n n-for no")
                        pass_response = input()
                        if pass_response == 'y':
                            print("Enter the length of your desired password in numerical digits")
                            length = int(input())
                            pass_word = get_password(length)
                            print("-"*50)
                            print(f"Password for {account} is {pass_word}")
                            print('\n')
                        elif pass_response == 'n':
                            print('\n')
                            print("Please enter your desired password...")
                            pass_word = input()
                        else:
                            print("Please enter a valid choice")

                        save_credential(create_credential(account, user_name, pass_word))
                        print("Your account has been saved")

                    elif short_code == 'dl':
                        print("Enter the credentials account you want to delete:...")
                        bin_credentials = input()

                        if check_existing_credential(bin_credentials):
                            print('\n')
                            print(f"Are you sure you want to delete {bin_credentials}? y/n")
                            bin_response = input()

                            if bin_response == 'y':
                                print('\n')
                                print(f"Your account for {bin_credentials} has been deleted")
                                deleted_cred = find_credential(bin_credentials)
                                del_credential(deleted_cred)
                            elif bin_response == 'n':
                                print('\n')
                                print(f"Noted. We're keeping {bin_credentials}")
                                print('\n')
                            else:
                                print('\n')
                                print("Invalid choice. Please enter a valid short-code")
                                print('\n')

                        else:
                            print('\n')
                            print("Sorry, you don't have that account saved in our system")
                            print('\n')

                    elif short_code == 'vw':
                        if display_credentials():
                            print('\n')
                            print("Here is a list of your account credentials")
                            print('\n')

                            for credentials in display_credentials():
                                print('\n')
                                print(f"Username: {credentials.user_name},Account/app: {credentials.account}, password: {credentials.pass_word}")
                                print('\n')
                        else:
                            print('\n')
                            print("Sorry, you dont seem to have any saved credentials")
                            print('\n')

                    elif short_code == 'x':
                        print('\n')
                        print("-"*50)
                        print("You have logged out.Goodbye!")
                        break

                    else:
                        print('\n')
                        print("please use proper short codes")
                        print('\n')

            else:
                print('\n')
                print("You don't have a password locker account yet. Create one by signing up. Use shortcode s")
                print('\n')

        elif option_chosen == 'x':
            print("Goodbye!")
            break

        else:
            print("Sorry, I didn't get that. Please use proper short codes")

        


                    





if __name__ == '__main__':
    main()



