
class TestClassExample():

    def test_type_example(self):
        assert type(1)==int

    def test_str_type(self):
        assert str.upper('python')=='PYTHON'
        assert str.lower('Python')=='python'
        # capitalize is a method that capitalized the first alphabet in the string.
        # example: the 'pytest'.capitalize() will give the output as Pytest
        assert 'pytest'.capitalize()=='pytest'