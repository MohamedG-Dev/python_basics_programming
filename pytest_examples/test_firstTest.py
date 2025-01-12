
def test_first_method():
    assert 5+5==10

# this is a failed test
def test_second_method():
    assert 7 > 9, '7 is not greater than 9'

def test_thirds_method():
    assert 9//5 == 1,'the result is incorrect' #integer truncating division