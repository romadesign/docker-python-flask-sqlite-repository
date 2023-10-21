from src.domain.model.test import Test


class TestInteractor:
    def __init__(self, config, test_repository):
        self.config = config
        self.test_repository = test_repository

    def get_all_tests(self):
        return self.test_repository.get_all_tests()

