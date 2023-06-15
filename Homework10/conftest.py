import pytest
import time


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    print('Время выполнения класса: {} sec'.format(end_time - start_time))


@pytest.fixture()
def test_fixture():
    start_time = time.time()
    yield
    end_time = time.time()
    print('Время выполнения теста: {} sec'.format(end_time - start_time))
