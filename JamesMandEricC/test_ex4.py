
import ex4
reload(ex4)

def  mod_myvar():
#Test 1
    myvar = 2
    expected = 4
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

#Test 2
    myvar = 3
    expected = 2
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)
#Test 3
    myvar = 4
    expected = 8
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)
###Test 4
    myvar = 5
    expected = 9
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

def compare_expected_and_actual(myvar, expected, actual):
    if expected == actual:
        print 'PASSED: For myvar =', myvar
    else:
        fmt = 'FAILED: For mayvar = {}\nExpected: {}\nActual:   {}'
        print fmt.format(myvar, expected, actual)

mod_myvar()
