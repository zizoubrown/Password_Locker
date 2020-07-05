class User:

    '''
    Class that generates new instances of user accounts
    '''

    user_account = [] # Empty user account

    def __init__(self, first_name, last_name, password, email):
        
        '''
        __init__ method that helps us define new properties for our objects
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def save_user(self):
        
        '''
        save_user method saves user account objects into user_account
        '''

        User.user_account.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user account from the user_account
        '''

        User.user_account.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):

        '''
        Method that takes in a first name and returns a user account that matches that first name
        '''

        for user in cls.user_account:
            if user.first_name == first_name:
                return user

    @classmethod
    def display_users(cls):

        '''
        method that returns the user_account
        '''

        return cls.user_account