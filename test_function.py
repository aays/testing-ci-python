import function

# in Python, 'test_' must preface whatever's being tested

def test_add_nums():
    added = function.add_nums(2, 2)
    assert added == 4
