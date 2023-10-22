# file: src/domain/interactor/user_interactor.py
from src.domain.model.user import create_user_from_dict

from src.lib.errors import NotAuthorizedError
from src.lib.errors import NotFoundError
from src.lib.errors import ForbiddenError

# from src.lib.validations import validate_required_fields
from src.domain.model.user import User, hash_password


class UserInteractorTest:
    def __init__(self, config, user_repository_test):
        self.config = config
        self.user_repository_test = user_repository_test

    def auth_user(self, username, password):
        user = self.user_repository_test.get_by_username(username)

        if user is None or not user.check_password(password):
            raise NotAuthorizedError({"msg": "Bad username or password"})

        return user

    
    def get_current_user(self):
        return self.user_repository_test.get_current_user()
    

    def get_current_user_data_none(self):
        return None


    def get_user_by_id(self, id):
        user = self.user_repository_test.get_user_by_id(id)
        if user is None:
            raise NotFoundError({"msg": "User not found"})

        return user

    def get_all_users(self):
        return self.user_repository_test.get_all_users()

    def get_user_by_username(self, username):
        user = self.user_repository_test.get_user_by_username(username)
        if user is None:
            raise NotFoundError({"msg": "User not found"})
        return user
    
    # def register_user(self, data):
    #     validate_required_fields(data, ["id", "username", "password", "name", "phone_number", "e_mail", "address"])
    #     user = User(data["id"], data["username"],  hash_password(data["password"]), data["name"], data["phone_number"], data["e_mail"], data["address"])
    #     self.user_repository_test.register_user(user)
    def save_user(self, data):
        # user = self.user_repository_test.get_current_user()

        # if user is None or not user.user_rol == "admin":
        #     raise ForbiddenError({"msg": "You are not admin"})

        # return user
        new_user = create_user_from_dict(data)
        return self.user_repository_test.save_user(new_user)

    def get_current_admin(self):
        user = self.user_repository_test.get_current_user()
        if user is None or not user.user_rol == "admin":
            raise ForbiddenError(
                {
                    "msg": "You are not admin",
                    "user_rol" : user.user_rol
                })

        return user

    

