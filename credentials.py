import pyperclip

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__(self, account, username, password):
        '''
        __init__ method that helps us define properties for credential objects
        
        Args:
            account: name app that user has opened account in
            username: username of user in that app
            password: password that the user has set for that account
        '''

        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method to save objects into credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        method that deletes a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_account(cls, acc):
        '''
        Method that takes in an account name and returns credentials matching that account
        
        Args:
            acc: name of app account to search for
        Returns:
            Credentials of user that matches that account name
        '''

        for credential in cls.credentials_list:
            if credential.account == acc:
                return credential

    @classmethod
    def credentials_exist(cls, acc):
        '''
        Method that checks of a credential exists in the credentials list
        
        Args:
            acc: name of app account to search for
        Returns:
            Boolean: True or False depending if the contact exists
        '''

        for credential in cls.credentials_list:
            if credential.account == acc:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_details(cls, acc):
        '''
        method to copy account details to machine clipboard using pyperclip
        '''
        credential_found = Credentials.find_by_account(acc)
        pyperclip.copy(credential_found.username)


