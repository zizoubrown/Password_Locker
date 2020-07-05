import unittest #importing the unittest module
from credential import Credential #importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test case defines test cases for the credential class behaivors
    '''
    def setUp(self):

        '''
        set up to run before each test case
        '''

        self.new_credential = Credential('Abdul','Instagram','z.i.z.o.u1','@!#') # create new credential object

    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.name,'Abdul')
        self.assertEqual(self.new_credential.social_media,'Instagram')
        self.assertEqual(self.new_credential.user_name,'z.i.z.o.u1')
        self.assertEqual(self.new_credential.password,'@!#')

    def test_save_credential(self):
        '''
        test_save_credential test case to test if the user credential is saved into the credential_list
        '''

        self.new_credential.save_credential() #save new user credential
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case is run
        '''

        Credential.credential_list = []

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple user credential
        '''

        self.new_credential.save_credential()
        test_credential = Credential('Majid','Snapchat','jidmore','abcd')
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)
        
    def test_delete_credential(self):
        '''
        test_delete_credential to test if we can remove a user credential from our credential_list
        '''

        self.new_credential.save_credential()
        test_credential = Credential('Majid','Snapchat','jidmore','abcd')
        test_credential.save_credential()

        self.new_credential.delete_credential() #Deleting a user credential object
        self.assertEqual(len(Credential.credential_list),1)

    def test_find_credential_by_user_name(self):
        '''
        test to check if we can find a user credential by the username and displays information
        '''

        self.new_credential.save_credential()
        test_credential = Credential('Majid','Snapchat','jidmore','abcd')
        test_credential.save_credential()

        found_credential = Credential.find_by_user_name('jidmore')

        self.assertEqual(found_credential.social_media,test_credential.social_media)
        
    def test_display_all_credential(self):
        '''
        method that returns a list of user credentials saved
        '''

        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()