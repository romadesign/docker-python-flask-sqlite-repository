# file: test/users/test_user_get_current_user.py
import pytest
import sqlite3


from src.domain.repository.user_repository import UserRepository
from src.domain.interactor.user_interactor import UserInteractor
from src.lib.errors import NotFoundError


def test_current_user_should_return_user_if_logged(database):

    # definimos una función "mock" para instanciar el repositorio
    # y actuar como si estuviera activo el usuario con id "user-1"

    def fake_get_user_id():
        return "user-1"

    user_repository = UserRepository(
        None, database, get_current_user_id=fake_get_user_id
    )
    interactor = UserInteractor(None, user_repository)

    user = interactor.get_current_user()
    assert user.id == "user-1"
    assert user.username == "user-1@example.com"
    assert user.name == "User 1"
    assert user.user_rol == "admin"
    assert user.phone_number == "223366895"
    assert user.e_mail == "user-1@example.com"
    assert user.address == "bilbao"
    assert user.destination_province_code == "48"
    assert user.destination_city_code == "002"



def test_current_user_should_return_None_if_not_logged(database):
    user_repository = UserRepository(None, database, lambda: None)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None


def test_current_user_should_return_None_if_not_id_getter_function(database):
    user_repository = UserRepository(None, database)
    interactor = UserInteractor(None, user_repository)

    assert interactor.get_current_user() is None

def test_get_user_by_id_should_raise_error_404_if_there_is_no_data(database):

    user_repository = UserRepository(None, database)
    user_interactor = UserInteractor(None, user_repository)

    with pytest.raises(NotFoundError):
        user_interactor.get_user_by_id("non existent id")


def test_get_user_by_id(database):

    user_repository = UserRepository(None, database)
    user_interactor = UserInteractor(None, user_repository)

    requested_user = user_interactor.get_user_by_id("user-1")

    assert requested_user.id == "user-1"

    requested_user = user_interactor.get_user_by_id("user-2")

    assert requested_user.id == "user-2"

def test_get_all_users(database):

    user_repository = UserRepository(None, database)
    user_interactor = UserInteractor(None, user_repository)

    all_users = user_interactor.get_all_users()

    assert len(all_users) == 4

# def test_get_user_by_username_should_raise_error_404_if_there_is_no_data(database):

#     user_repository = UserRepository(None, database)
#     user_interactor = UserInteractor(None, user_repository)

#     with pytest.raises(NotFoundError):
#         user_interactor.get_user_by_username("non existent username")

def test_get_user_by_username_if_they_exist(database):
    user_repository = UserRepository(None, database)
    user_interactor = UserInteractor(None, user_repository)
    user_by_username = user_interactor.get_user_by_username("user-1@example.com")

    assert user_by_username.id == "user-1"
    assert user_by_username.username == "user-1@example.com"
    assert user_by_username.name == "User 1"
    assert user_by_username.password == "96ace8d36b7a2c1423aa3886b70101fab26c0cd22733bdd78bc64aa88e56c560"
    assert user_by_username.e_mail == "user-1@example.com"
    assert user_by_username.phone_number == "223366895"
    assert user_by_username.address == "bilbao"
    assert user_by_username.user_rol == "admin"
    assert user_by_username.destination_province_code == "48"
    assert user_by_username.destination_city_code == "002"
    




