import hashlib
# from src.lib.validations import validate_required_fields


def hash_password(password):
    hash_obj = hashlib.sha256(password.encode())
    return hash_obj.hexdigest()


class User:
    def __init__(self, id, username, name, password, user_rol, phone_number, e_mail, address):
        self.id = id
        self.username = username
        self.name = name
        self.password = password
        self.user_rol = user_rol
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.address = address

    def check_password(self, password):
        return hash_password(password) == self.password

    def __getstate__(self):

        # not sending "password" when instance is "jsonified"

        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "user_rol": self.user_rol,
            "phone_number": self.phone_number,
            "e_mail": self.e_mail,
            "address": self.address
        }


def create_user_from_dict(data):
    password = hash_password(data["password"])
    return User(
        data["id"],
        data["username"],
        data["name"],
        password,
        data["user_rol"],
        data["phone_number"],
        data["e_mail"],
        data["address"],
    )
