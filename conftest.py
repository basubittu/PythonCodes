import pytest


@pytest.fixture(scope="function")
def showCheck():
    print("Inside data")
    yield
    print("Outside data")
