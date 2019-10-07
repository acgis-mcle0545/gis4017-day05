def is_divisble(numerator, denominator):


    if isinstance(denominator, str):
        return False
    else:
     if numerator % denominator == 0:
        return True
     else:
        return False

    if (numerator.isdigit()) and (denominator.isdigit()) == False:
        return (int(numerator)) and (int(denominator))
        if numerator % denominator == 0:
            return True
        else:
            return False

##        if str(numerator) % str(denominator) == 0:
##            return True
##        else:
##            return False


##       if numerator.isdigit() % denominator.isdigit() == 0:
##        return True
##       else:
##        return False




