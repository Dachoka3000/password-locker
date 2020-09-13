import unittest
from user import User

class TestUser (unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run
        '''
        User.user_list = []

    def setUp(self):
        '''
        Set up method to run before each test case
        '''

        self.new_user = User("Daisy Day", "daisy@email.com", "me123")

    def test_init(self):
        '''
        test_init test case to test if the object is initialised properly
        '''

        self.assertEqual(self.new_user.username, "Daisy Day")
        self.assertEqual(self.new_user.email, "daisy@email.com")
        self.assertEqual(self.new_user.password, "me123")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple usesrs into the user lists
        '''

        self.new_user.save_user()
        test_user = User("Test user", "test@user.com", "012345")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by their username and display information
        '''
        self.new_user.save_user()
        test_user = User("Test user", "test@user.com", "012345")
        test_user.save_user()

        found_user = User.find_by_username("Test user")

        self.assertEqual(found_user.email, test_user.email)

    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we find a user or not
        '''

        self.new_user.save_user()
        test_user = User("Test user", "test@user.com", "012345")
        test_user.save_user()

        user_exists = User.user_exist("Test user")

        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()