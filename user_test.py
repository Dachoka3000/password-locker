import unittest
from user import User

class TestUser (unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.
    
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

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

if __name__ == '__main__':
    unittest.main()