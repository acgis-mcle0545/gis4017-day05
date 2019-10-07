import ex1
reload(ex1)

def main():
    """main()"""
    expected = 'POINT'
    arg = 1
    actual = ex1.get_feature_type(arg)
    compare_expected_and_actual(arg, expected, actual)
    expected = 'POLYLINE'
    arg = 2
    actual = ex1.get_feature_type(arg)
    compare_expected_and_actual(arg, expected, actual)
    expected = 'POLYGON'
    arg = 3
    actual = ex1.get_feature_type(arg)
    compare_expected_and_actual(arg, expected, actual)

def compare_expected_and_actual(arg, expected, actual):
    if expected == actual:
        print 'PASSED:  For arg=', arg
    else:
        fmt = 'FAILED: For arg = {}\nExpected: {}\nActual:   {}'
        print fmt.format(arg, expected, actual)

if __name__ == '__main__':
    main()
