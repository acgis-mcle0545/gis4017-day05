
import ex3
reload(ex3)

def  is_point_in_on_line():

    m=2
    b=3
#Test 1
    expected = False
    x = 0
    y = 2
    actual = ex3.is_point_on_line (x, y, m, b)
    compare_expected_and_actual(x, y, expected, actual)

#Test 2
    expected = False
    x=5
    y=44
    actual = ex3.is_point_on_line (x, y, m, b)
    compare_expected_and_actual(x, y, expected, actual)
#Test 3
    expected = False
    x=1
    y=4
    actual = ex3.is_point_on_line (x, y, m, b)
    compare_expected_and_actual(x, y, expected, actual)
#Test 4
    expected = True
    x=0
    y=3
    actual = ex3.is_point_on_line (x, y, m, b)
    compare_expected_and_actual(x, y, expected, actual)


def compare_expected_and_actual(x, y, expected, actual):
    if expected == actual:
        print 'PASSED:  For x,y =', x, y
    else:
        fmt = 'FAILED: For x,y = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(x, y, expected, actual)

is_point_in_on_line()