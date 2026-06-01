from django.contrib.auth.models import User
from django.db import IntegrityError
from CoreUtils.Logger import Logger



class Authentication_handler():

    def __init__(self, user_data):
        self.username = user_data['username']
        self.email = user_data['email']
        self.password = user_data['password']
        self.createLog = Logger()


    def create_account(self):
        try:
            if User.objects.filter(email=self.email).exists() :
                return {
                        'user_exist': 'email already linked with an account'
                        }
            if User.objects.filter(username=self.username).exists():
                return {
                        'user_exist': 'username already taken'
                        }

            user_object = User.objects.create_user(
                    username = self.username,
                    email = self.email,
                    password = self.password
                    )

            user_object.save()

            return {'created': 'account created'}

        except IntegrityError as e:
            self.createLog.Log_Error(f'Authentication_Handler_Exception', e)
            return {'error': e}
            




