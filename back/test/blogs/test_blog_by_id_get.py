import pytest
from src.lib.errors import NotAuthorizedError
from src.domain.repository.blog_repository import BlogRepository
from src.domain.interactor.blog_interactor import BlogInteractor
from src.lib.sqlite_based_repository import SqliteBasedRepository


def test_should_get_None_if_no_data(database):

    blog_repository = BlogRepository(None, database)
    interactor = BlogInteractor(None, blog_repository)

    blog = interactor.get_all_blogs()


def test_should_download_blogs_if_exist(database):

    blog_repository = BlogRepository(None, database)
    blog_interactor = BlogInteractor(None, blog_repository)
    all_blogs = blog_interactor.get_all_blogs()
    assert len(all_blogs) == 2
    assert all_blogs[0].id == "blog-id-1"
    assert all_blogs[0].blogtype == "blog-service-type-1"
    assert all_blogs[0].title == "blog-title-1"
    assert all_blogs[0].image == "blog-image-1"
    assert all_blogs[0].price == "blog-price-1"
    assert all_blogs[0].user_id == "blog-user-id-1"
    assert all_blogs[0].start_time == "blog-start-time-1"
    assert all_blogs[0].end_time == "blog-end-time-1"
    assert all_blogs[0].address == "bilbao"

    assert all_blogs[1].id == "blog-id-2"
    assert all_blogs[1].blogtype == "blog-service-type-2"
    assert all_blogs[1].title == "blog-title-2"
    assert all_blogs[1].image == "blog-image-2"
    assert all_blogs[1].price == "blog-price-2"
    assert all_blogs[1].user_id == "blog-user-id-2"
    assert all_blogs[1].start_time == "blog-start-time-2"
    assert all_blogs[1].end_time == "blog-end-time-2"
    assert all_blogs[1].address == "casco viejo"


def test_should_get_recipe_if_data(database):

    # Arrange

    blog_repository = BlogRepository(None, database)
    interactor = BlogInteractor(None, blog_repository)

    # Act

    blog_1 = interactor.get_blog_by_id("blog-id-1")
    blog_2 = interactor.get_blog_by_id("blog-id-2")

    # Assert

    assert blog_1.id == "blog-id-1"
    assert blog_1.blogtype == "blog-service-type-1"
    assert blog_1.title == "blog-title-1"
    assert blog_1.image == "blog-image-1"
    assert blog_1.price == "blog-price-1"
    assert blog_1.user_id == "blog-user-id-1"
    assert blog_1.start_time == "blog-start-time-1"
    assert blog_1.end_time == "blog-end-time-1"

    assert blog_1.id == "blog-id-1"
    assert blog_1.blogtype == "blog-service-type-1"
    assert blog_1.title == "blog-title-1"
    assert blog_1.image == "blog-image-1"
    assert blog_1.price == "blog-price-1"
    assert blog_1.user_id == "blog-user-id-1"
    assert blog_1.start_time == "blog-start-time-1"
    assert blog_1.end_time == "blog-end-time-1"


def test_update_recipe_if_exists_if_not_post_it(database):

    blog_repository = BlogRepository(None, database)
    blog_interactor = BlogInteractor(None, blog_repository)

    data = {
        "id": "blog-1",
        "blogtype": "unknown blog",
        "title": "unknown blog",
        "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII=",
        "price": "3$",
        "user_id": "user_1",
        "start_time": "15/05/2021 00:02",
        "end_time": "16/06/2021 15:00",
    }
    blog_interactor.save_blog(data)

    blog = blog_interactor.get_blog_by_id("blog-1")

    assert blog.id == "blog-1"
    assert blog.blogtype == "unknown blog"
    assert blog.title == "unknown blog"
    assert blog.image == "/images/blog-1.png"
    assert blog.price == "3$"
    assert blog.user_id == "user_1"
    assert blog.start_time == "15/05/2021 00:02"
    assert blog.end_time == "16/06/2021 15:00"
    assert blog.address == "deustu"
