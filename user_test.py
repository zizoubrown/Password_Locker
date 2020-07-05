import unittest #Importing the unittest module
from user import User #Impoerting the user class

class TestUser(unittest.TestCase):

    '''
    Test case defines test cases for the user class behaviours
    '''
    def setUp(self):

        '''
        set up to run before each test cases.
        '''
        self.new_user = User('Abdul','Aziz','#?/','zizumoha2015@gmail.com') #create new user account object


    def test_init(self):
        '''
        test_init to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,'Abdul')
        self.assertEqual(self.new_user.last_name,'Aziz')
        self.assertEqual(self.new_user.password,'#?/')
        self.assertEqual(self.new_user.email,'zizumoha2015@gmail.com')

    def test_save_user(self):
        '''
        test_save_user test case to test if the user account object is saved into user_account
        '''

        self.new_user.save_user() # saving the new user account
        self.assertEqual(len(User.user_account),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case is run
        '''

        User.user_account = []

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user account
        '''

        self.new_user.save_user()
        test_user = User('Mahamed','Mahamud','&*&*','mahamed@gmail.com')
        test_user.save_user()
        self.assertEqual(len(User.user_account),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user account from our user_account list
        '''

        self.new_user.save_user()
        test_user = User('Mahamed','Mahamud','&*&*','mahamed@gmail.com')
        test_user.save_user()

        self.new_user.delete_user() # Deleting a user account object
        self.assertEqual(len(User.user_account),1)

    def test_find_user_by_first_name(self):
        '''
        test to check if we can find a user account by first name and display information
        '''

        self.new_user.save_user()
        test_user = User('Mahamed','Mahamud','&*&*','mahamed@gmail.com')
        test_user.save_user()

        found_user = User.find_by_first_name('Mahamed')

        self.assertEqual(found_user.email,test_user.email) # check if the user account object is equal to the saved user account

    def test_display_all_user(self):
        '''
        method that returns a list of all user accounts saved
        '''

        self.assertEqual(User.display_users(),User.user_account)


if __name__ == '__main__':
    unittest.main()