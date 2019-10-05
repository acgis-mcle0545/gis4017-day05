import ex6
reload(ex6)

def is_numeric():
##
##    test_string = '123'
##    expected = True
##    actual = ex6.is_numeric (test_string)
##    compare_expected_and_actual(test_string, expected, actual)

    test_string = '-18788'
    expected = True
    actual = ex6.is_numeric (test_string)
    compare_expected_and_actual(test_string, expected, actual)

    test_string = '-0.18788'
    expected = False
    actual = ex6.is_numeric (test_string)
    compare_expected_and_actual(test_string, expected, actual)

    test_string = '.18788'
    expected = False
    actual = ex6.is_numeric (test_string)
    compare_expected_and_actual(test_string, expected, actual)

def compare_expected_and_actual(test_string, expected, actual):
    if expected == actual:
        print 'PASSED:  For test string =', test_string
    else:
        fmt = 'FAILED: For test string = {}, \nExpected: {}\nActual:   {}'
        print fmt.format(test_string, expected, actual)

is_numeric()

