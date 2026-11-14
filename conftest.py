import pytest


@pytest.fixture(scope="function")
def showCheck():
    print("Inside data")
    yield
    print("Outside data")

@pytest.fixture(scope="module")
def showData():
    print("Fixure Function")

@pytest.fixture(scope="function")
def loopdata():
    for i in range (1,11):
        print("The value is",i)