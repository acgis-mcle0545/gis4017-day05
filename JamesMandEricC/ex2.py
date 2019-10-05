def is_point_in_box(x, y, xmin, ymin, xmax, ymax):

    if (xmin < x < xmax) and (ymin < y < ymax):
        return True
    elif ymax or ymin == y:
        return False
    elif xmin or xmax == x:
        return False
    elif xmin >= x >= xmax:
       return False
    elif ymin >= y >= ymax:
        return False




