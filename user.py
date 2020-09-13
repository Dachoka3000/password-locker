class User:
    '''
    Class that generates new instances of Users
    '''

    user_list = []

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

    def save_user(self):
        '''
        save_user method saves user objects into the user_list
        '''
        User.user_list.append(self)

    @classmethod
    def find_by_username(cls, uname):
        '''
        Method that takes in a name and returns a user that matches that name
        
        Args:
            uname: user name to search for
        Returns;
            user account that matches that username
        '''

        for user in cls.user_list:
            if user.username == uname:
                return user

    @classmethod
    def user_exist(cls, uname):
        '''
        Method that checks if a user exists from the user list
        
        Args:
            uname: username to search if a user exists
        Returns:
            Boolean: True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.username == uname:
                return True
        return False
            
