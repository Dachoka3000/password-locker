import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        tearDown method that cleans up after each tesst case is run
        '''
        Credentials.credentials_list = []

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

    def test_save_credentials(self):
        '''
        test_save_credentials to test if the credentials objects are saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can saave multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Instagram", "Muse Art", "museart1000")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test to check if we can delete credentials from the credentials list
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Instagram", "Muse Art", "museart1000")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find credentials by account and display information
        '''

        self.new_credentials.save_credentials()
        test_credential = Credentials("Snapchat", "Test User", "user195")
        test_credential.save_credentials()

        found_credential = Credentials.find_by_account("Snapchat")

        self.assertEqual(found_credential.password, test_credential.password)





if __name__ == '__main__':
    unittest.main()


