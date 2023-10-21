import pytest
import sqlite3
from src.domain.interactor.recipe_interactor import RecipeInteractor
from src.domain.repository.recipe_repository import RecipeRepository


def test_should_get_empty_list_if_no_data(database):
    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    all_provinces = recipe_interactor.get_all_provinces()
    assert all_provinces == []


def test_should_get_all_provinces_if_data(database):
    database.executescript(
        """
        INSERT INTO provinces (province_code, province_name) VALUES
            ("1", "name-1"),
            ("2", "name-2");
        """
    )
    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    all_provinces = recipe_interactor.get_all_provinces()
    assert all_provinces[0].code == "1"
    assert all_provinces[0].name == "name-1"
    assert all_provinces[1].code == "2"
    assert all_provinces[1].name == "name-2"
