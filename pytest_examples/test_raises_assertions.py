import pytest
def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert 1/0

def test_case02():
    with pytest.raises(Exception) as exception_info:
        # assert (1,2,3)==(1,2,4)
        func_01()
        print(str(exception_info))
        assert (str(exception_info))=='raised exception in function 01'

def func_01():
    raise ValueError('raised exception in function 01')