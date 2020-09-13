class User:
    '''
    Class that generates new instances of Users
    '''

    def __init__(self, username, email, password):
        '''
        __init__ method that helps define properties for a user instance
        
        Args:
            username: username of a user when opening an account
            email: email address of a user
            password: password of a user for their account
        '''

        self.username = username
        self.email = email
        self.password = password
