def is_numeric (test_string):

##    if isinstance(test_string, int):

    if test_string.isdigit():
        return True
    elif (test_string[1:].isdigit()) and (test_string[0] == '-'):
        return True
    else:
         return False




# if it is negative, no decminal return true

#if it has any . return false

