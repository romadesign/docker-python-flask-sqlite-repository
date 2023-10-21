import pytest
import sqlite3
from src.domain.interactor.recipe_interactor import RecipeInteractor
from src.domain.repository.recipe_repository import RecipeRepository
from src.lib.errors import NotFoundError


def test_should_get_empty_list_if_no_data(database):
    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    all_provinces = recipe_interactor.get_all_provinces()
    assert all_provinces == []


def test_should_get_NotFoundError_if_the_province_doesnt_exist(database):
    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    with pytest.raises(NotFoundError) as exception:
        all_cities = recipe_interactor.get_all_cities_by_province_code(
            "province-not-exists"
        )
    assert exception.value.data == {
        "msg": "Province with code 'province-not-exists' not found."
    }


def test_should_get_all_cities_from_the_specified_province_if_data(database):
    database.executescript(
        """
        INSERT INTO provinces (province_code, province_name) VALUES
            ("province-1", "province-name-1"),
            ("province-2", "province-name-2");
        INSERT INTO cities (province_code, city_code, city_name) VALUES
            ("province-1", "city-1", "city-name-1"),
            ("province-1", "city-2", "city-name-2"),
            ("province-2", "city-3", "city-name-3")
        """
    )
    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    all_cities = recipe_interactor.get_all_cities_by_province_code("province-1")
    assert all_cities[0].province_code == "province-1"
    assert all_cities[0].city_code == "city-1"
    assert all_cities[0].city_name == "city-name-1"
    assert all_cities[1].province_code == "province-1"
    assert all_cities[1].city_code == "city-2"
    assert all_cities[1].city_name == "city-name-2"
