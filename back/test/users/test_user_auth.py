import pytest  # type: ignore

from src.domain.repository.user_repository_test import UserRepositoryTest
from src.domain.interactor.user_interactor_test import UserInteractorTest

from src.lib.errors import NotAuthorizedError


def test_auth_user_should_return_user_if_password_is_ok(database):
    user_repository = UserRepositoryTest(None, database, lambda: "user-1")
    interactor = UserInteractorTest(None, user_repository)

    user = interactor.auth_user("user-1@example.com", "newtest1")
    assert user.id == "user-1"
    assert user.username == "user-1@example.com"
    assert user.name == "User 1"
    assert user.user_rol == "admin"
    assert user.phone_number == "223366895"
    assert user.e_mail == "user-1@example.com"
    assert user.address == "bilbao"


def test_auth_user_should_raise_unauthorized_if_user_is_unknown(database):
    user_repository = UserRepositoryTest(None, database, lambda: "user-1")
    interactor = UserInteractorTest(None, user_repository)

    with pytest.raises(NotAuthorizedError):
        interactor.auth_user("user-unknown@example.com", "user-1-bad-password")


def test_auth_user_should_raise_unauthorized_if_password_not_ok(database):
    user_repository = UserRepositoryTest(None, database, lambda: "user-1")
    interactor = UserInteractorTest(None, user_repository)

    with pytest.raises(NotAuthorizedError):
        interactor.auth_user("user-1@example.com", "user-1-bad-password")

