
import ex4
reload(ex4)

def  mod_myvar():

##Assignemnt 1 Test Begin:###
##    myvar = 1
##    expected = 5
##    actual = ex4.mod_myvar (myvar)
##    compare_expected_and_actual(myvar, expected, actual)
##
##    myvar = 5
##    expected = 9
##    actual = ex4.mod_myvar (myvar)
##    compare_expected_and_actual(myvar, expected, actual)
##
##    myvar = 7
##    expected = 11
##    actual = ex4.mod_myvar (myvar)
##    compare_expected_and_actual(myvar, expected, actual)
##
##    myvar = 9
##    expected = 13
##    actual = ex4.mod_myvar (myvar)
##    compare_expected_and_actual(myvar, expected, actual)

##Assignemnt 2 Test Begin:###

    myvar = 3
    expected = 2
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

### ** 3 != 27 can only have 1 test because 3*3*3 is the only = 27

##Assignemnt 3 Test Begin:###
    myvar = 2
    expected = 4
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 4
    expected = 8
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 6
    expected = 12
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 8
    expected = 16
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

###Assignent 4###

    myvar = 12
    expected = 10
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 14
    expected = 12
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 16
    expected = 14
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)

    myvar = 18
    expected = 16
    actual = ex4.mod_myvar (myvar)
    compare_expected_and_actual(myvar, expected, actual)


def compare_expected_and_actual(myvar, expected, actual):
    if expected == actual:
        print 'PASSED: For myvar =', myvar
    else:
        fmt = 'FAILED: For mayvar = {}\nExpected: {}\nActual:   {}'
        print fmt.format(myvar, expected, actual)

mod_myvar()
