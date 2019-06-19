# challenges
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a,b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} is in {1}".format(item, collection)
    
def test_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)

test_not_equal(5,4)

test_is_in([5,7,89], 5)

test_not_in([3,9,601,56,12], 4)

test_between(10, 3, 7)
print("all tests passed!")