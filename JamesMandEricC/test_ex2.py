import ex2
reload(ex2)

def is_point_in_box():

    xmin = 1
    ymin = 1
    xmax = 10
    ymax = 10

    expected = False
    x = 1
    y = 5
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 5
    y = 10
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 10
    y = 5
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 5
    y = 1
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 10
    y = 5
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 5
    y = 10
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = False
    x = 12
    y = 12
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

    expected = True
    x = 6
    y = 6
    actual = ex2.is_point_in_box (x, y, xmin, ymin, xmax, ymax)
    compare_expected_and_actual(x, y, expected, actual)

def compare_expected_and_actual(x, y, expected, actual):
    if expected == actual:
        print 'PASSED:  For x,y =', x, y
    else:
        fmt = 'FAILED: For x,y = {}, {}\nExpected: {}\nActual:   {}'
        print fmt.format(x, y, expected, actual)

is_point_in_box()