def mod_myvar(myvar):
    if myvar % 2:
        if myvar ** 3 != 27:
            myvar += 4           # Assignment statement 1
        else:
            myvar /= 1.5         # Assignment statement 2
    else:
        if myvar <= 10:
            myvar *= 2           # Assignment statement 3
        else:
            myvar -= 2           # Assignment statement 4
    return myvar
