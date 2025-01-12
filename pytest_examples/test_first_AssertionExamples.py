
def test_assert_first_method():
    assert 4 <=5

def test_assert_second_method():
    # assert 1 is equals assert True
    assert 1

def test_assert_third_method():
    assert "abcd"=='abcd'

def test_assert_arithmetic_operation():
    # The below scenario will fail the test case, to pass the case give expected value as 1.0
    # instead of 2.0
    assert (3-1*4/2)==2.0

def test_assert_arithmetic_operation_divmod():
    assert 1 in divmod(9,5)
    assert 'py' in 'this is pytest'
    assert 'pout' not in 'this is pytest'
    # we cannot compare the sublist with a list, but we can compare a value inside a list.
    assert [1,2] in [1,2,4]