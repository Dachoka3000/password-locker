import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_credentials = Credentials("Twitter", "MaryX", "maryx1000")

    def test_init(self):
        '''
        test_init test case to test if the object is initialised correctly
        '''

        self.assertEqual(self.new_credentials.account, "Twitter")
        self.assertEqual(self.new_credentials.username, "MaryX")
        self.assertEqual(self.new_credentials.password,"maryx1000")

if __name__ == '__main__':
    unittest.main()

