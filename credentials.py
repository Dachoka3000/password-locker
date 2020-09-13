class Credentials:
    '''
    Class that generates new instances of credentials
    '''
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