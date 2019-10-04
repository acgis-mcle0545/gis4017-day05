import ex5
reload(ex5)

def is_divisble():

    expected = False
    numerator = "123"
    denominator = "123"
    actual = ex5.is_divisble (numerator, denominator)
    compare_expected_and_actual (numerator, denominator, expected, actual)

    expected = True
    numerator = 7
    denominator = 7
    actual = ex5.is_divisble (numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

    expected = False
    numerator = 9
    denominator = 7
    actual = ex5.is_divisble (numerator, denominator)
    compare_expected_and_actual(numerator, denominator, expected, actual)

def compare_expected_and_actual(numerator, denominator, expected, actual):
    if expected == actual:
        print 'PASSED:  For numerator,denominator =', numerator, denominator
    else:
        fmt = 'FAILED: For numerator,denominator = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(numerator, denominator, expected, actual)

is_divisble()