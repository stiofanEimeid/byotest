# def number_of_evens(numbers):
#     return 0


# def test_are_equal(actual, expected):
#     assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
# challenges
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a,b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "Did not expect {0} to contain {1} but does".format(collection, item)
    
def test_between(a, b, c):
    assert a >= b and a <=c, "Expected True but got False"
    
    
# test_are_equal(number_of_evens([1,2,3,4,5]), 2)

test_not_equal(5,4)

test_is_in([5,7,89], 5)

test_not_in([3,9,601,56,12], 4)

test_between(7, 3, 10)
print("all tests passed!")