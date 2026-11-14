import pytest

@pytest.mark.smoke
def test_sumData():
    s=0;
    s=(50+80)
    print("The sum is",s)

@pytest.mark.dataCheck
def  test_multipledata():
    mul=(20*30)
    print(mul) 
    