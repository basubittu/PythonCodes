import pytest


@pytest.fixture
def showData():
    print("Fixure Function")


def test_newdata(showData):
    print("India")

def test_dataSet(showData):
    print("Pakistan")

def test_checkData(showData):
    assert(False)
    print("Inside show data")

