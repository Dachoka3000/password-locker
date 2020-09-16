import pyperclip

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__(self, account, user_name, pass_word):
        '''
        __init__ method that helps us define properties for credential objects
        
        Args:
            account: name app that user has opened account in
            username: username of user in that app
            password: password that the user has set for that account
        '''

        self.account = account
        self.user_name = user_name
        self.pass_word = pass_word

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
    def find_by_account(cls, account):
        '''
        Method that takes in an account name and returns credentials matching that account
        
        Args:
            acc: name of app account to search for
        Returns:
            Credentials of user that matches that account name
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def credentials_exist(cls, account):
        '''
        Method that checks of a credential exists in the credentials list
        
        Args:
            acc: name of app account to search for
        Returns:
            Boolean: True or False depending if the contact exists
        '''

        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_details(cls, account):
        '''
        method to copy account details to machine clipboard using pyperclip
        '''
        credential_found = Credentials.find_by_account(account)
        pyperclip.copy(credential_found.user_name)


