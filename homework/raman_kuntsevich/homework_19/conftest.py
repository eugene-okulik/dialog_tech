import pytest


@pytest.fixture(scope='session', autouse=True)
def print_before_and_after_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def print_before_and_after_tests():
    print('before test')
    yield
    print('after test')
