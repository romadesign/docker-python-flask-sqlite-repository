import pytest
from src.lib.errors import NotAuthorizedError
from src.domain.repository.recipe_repository import RecipeRepository
from src.domain.interactor.recipe_interactor import RecipeInteractor
from src.lib.sqlite_based_repository import SqliteBasedRepository


def test_should_get_None_if_no_data(database):

    recipe_repository = RecipeRepository(None, database)
    interactor = RecipeInteractor(None, recipe_repository)

    recipe = interactor.get_all_recipes()


def test_should_download_recipes_if_exist(database):

    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)
    all_recipes = recipe_interactor.get_all_recipes()
    assert len(all_recipes) == 2
    assert all_recipes[0].id == "recipe-id-1"
    assert all_recipes[0].categoryrecipe == "recipe-service-type-1"
    assert all_recipes[0].title == "recipe-title-1"
    assert all_recipes[0].image == "recipe-image-1"
    assert all_recipes[0].price == "recipe-price-1"
    assert all_recipes[0].user_id == "recipe-user-id-1"
    assert all_recipes[0].start_time == "recipe-start-time-1"
    assert all_recipes[0].end_time == "recipe-end-time-1"
    assert all_recipes[0].address == "bilbao"

    assert all_recipes[1].id == "recipe-id-2"
    assert all_recipes[1].categoryrecipe == "recipe-service-type-2"
    assert all_recipes[1].title == "recipe-title-2"
    assert all_recipes[1].image == "recipe-image-2"
    assert all_recipes[1].price == "recipe-price-2"
    assert all_recipes[1].user_id == "recipe-user-id-2"
    assert all_recipes[1].start_time == "recipe-start-time-2"
    assert all_recipes[1].end_time == "recipe-end-time-2"
    assert all_recipes[1].address == "casco viejo"


def test_should_get_recipe_if_data(database):

    # Arrange

    recipe_repository = RecipeRepository(None, database)
    interactor = RecipeInteractor(None, recipe_repository)

    # Act

    recipe_1 = interactor.get_recipe_by_id("recipe-id-1")
    recipe_2 = interactor.get_recipe_by_id("recipe-id-2")

    # Assert

    assert recipe_1.id == "recipe-id-1"
    assert recipe_1.categoryrecipe == "recipe-service-type-1"
    assert recipe_1.title == "recipe-title-1"
    assert recipe_1.image == "recipe-image-1"
    assert recipe_1.price == "recipe-price-1"
    assert recipe_1.user_id == "recipe-user-id-1"
    assert recipe_1.start_time == "recipe-start-time-1"
    assert recipe_1.end_time == "recipe-end-time-1"

    assert recipe_1.id == "recipe-id-1"
    assert recipe_1.categoryrecipe == "recipe-service-type-1"
    assert recipe_1.title == "recipe-title-1"
    assert recipe_1.image == "recipe-image-1"
    assert recipe_1.price == "recipe-price-1"
    assert recipe_1.user_id == "recipe-user-id-1"
    assert recipe_1.start_time == "recipe-start-time-1"
    assert recipe_1.end_time == "recipe-end-time-1"


def test_update_recipe_if_exists_if_not_post_it(database):

    recipe_repository = RecipeRepository(None, database)
    recipe_interactor = RecipeInteractor(None, recipe_repository)

    data = {
        "id": "recipe-1",
        "categoryrecipe": "unknown recipe",
        "title": "unknown recipe",
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=",
        "price": "3$",
        "user_id": "user_1",
        "start_time": "15/05/2021 00:02",
        "end_time": "16/06/2021 15:00",
    }
    recipe_interactor.save_recipe(data)

    recipe = recipe_interactor.get_recipe_by_id("recipe-1")

    assert recipe.id == "recipe-1"
    assert recipe.categoryrecipe == "unknown recipe"
    assert recipe.title == "unknown recipe"
    assert recipe.image == "/images/recipe-1.png"
    assert recipe.price == "3$"
    assert recipe.user_id == "user_1"
    assert recipe.start_time == "15/05/2021 00:02"
    assert recipe.end_time == "16/06/2021 15:00"
    assert recipe.address == "deustu"
