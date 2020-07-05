class Credential:

    '''
    class that generate new instance of user credentials
    '''

    credential_list = [] # Empty credential list

    def __init__(self,name,social_media,user_name,password):

        '''
        __init__ method that helps us define new propperties for our objects
        '''

        self.name = name
        self.social_media = social_media
        self.user_name = user_name
        self.password = password

    def save_credential(self):

        '''
        save_credential saves user credential objects into credential list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential  method deletes a saved user credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_user_name(cls,username):

        '''
        Method that takes in the username and returns a user credential that matches that username
        '''

        for credential in cls.credential_list:
            if credential.user_name == username:
                return credential

    @classmethod
    def display_credentials(cls):

        '''
        method that returns the credential_list
        '''

        return cls.credential_list
