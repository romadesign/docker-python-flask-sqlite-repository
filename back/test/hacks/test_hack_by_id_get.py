import pytest
from src.lib.errors import NotAuthorizedError
from src.domain.repository.hack_repository import HackRepository
from src.domain.interactor.hack_interactor import HackInteractor
from src.lib.sqlite_based_repository import SqliteBasedRepository


def test_should_get_None_if_no_data(database):

    hack_repository = HackRepository(None, database)
    interactor = HackInteractor(None, hack_repository)

    hack = interactor.get_all_hacks()


def test_should_download_hacks_if_exist(database):

    hack_repository = HackRepository(None, database)
    hack_interactor = HackInteractor(None, hack_repository)
    all_hacks = hack_interactor.get_all_hacks()
    assert len(all_hacks) == 2
    assert all_hacks[0].id == "hack-id-1"
    assert all_hacks[0].categoryhack == "hack-service-type-1"
    assert all_hacks[0].title == "hack-title-1"
    assert all_hacks[0].image == "hack-image-1"
    assert all_hacks[0].price == "hack-price-1"
    assert all_hacks[0].user_id == "hack-user-id-1"
    assert all_hacks[0].start_time == "hack-start-time-1"
    assert all_hacks[0].end_time == "hack-end-time-1"
    assert all_hacks[0].address == "bilbao"

    assert all_hacks[1].id == "hack-id-2"
    assert all_hacks[1].categoryhack == "hack-service-type-2"
    assert all_hacks[1].title == "hack-title-2"
    assert all_hacks[1].image == "hack-image-2"
    assert all_hacks[1].price == "hack-price-2"
    assert all_hacks[1].user_id == "hack-user-id-2"
    assert all_hacks[1].start_time == "hack-start-time-2"
    assert all_hacks[1].end_time == "hack-end-time-2"
    assert all_hacks[1].address == "casco viejo"


def test_should_get_hack_if_data(database):

    # Arrange

    hack_repository = HackRepository(None, database)
    interactor = HackInteractor(None, hack_repository)

    # Act

    hack_1 = interactor.get_hack_by_id("hack-id-1")
    hack_2 = interactor.get_hack_by_id("hack-id-2")

    # Assert

    assert hack_1.id == "hack-id-1"
    assert hack_1.categoryhack == "hack-service-type-1"
    assert hack_1.title == "hack-title-1"
    assert hack_1.image == "hack-image-1"
    assert hack_1.price == "hack-price-1"
    assert hack_1.user_id == "hack-user-id-1"
    assert hack_1.start_time == "hack-start-time-1"
    assert hack_1.end_time == "hack-end-time-1"

    assert hack_1.id == "hack-id-1"
    assert hack_1.categoryhack == "hack-service-type-1"
    assert hack_1.title == "hack-title-1"
    assert hack_1.image == "hack-image-1"
    assert hack_1.price == "hack-price-1"
    assert hack_1.user_id == "hack-user-id-1"
    assert hack_1.start_time == "hack-start-time-1"
    assert hack_1.end_time == "hack-end-time-1"


def test_update_hack_if_exists_if_not_post_it(database):

    hack_repository = HackRepository(None, database)
    hack_interactor = HackInteractor(None, hack_repository)

    data = {
        "id": "hack-1",
        "categoryhack": "unknown hack",
        "title": "unknown hack",
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=",
        "price": "3$",
        "user_id": "user_1",
        "start_time": "15/05/2021 00:02",
        "end_time": "16/06/2021 15:00",

    }
    hack_interactor.save_hack(data)

    hack = hack_interactor.get_hack_by_id("hack-1")

    assert hack.id == "hack-1"
    assert hack.categoryhack == "unknown hack"
    assert hack.title == "unknown hack"
    assert hack.image == "/images/hack-1.png"
    assert hack.price == "3$"
    assert hack.user_id == "user_1"
    assert hack.start_time == "15/05/2021 00:02"
    assert hack.end_time == "16/06/2021 15:00"
