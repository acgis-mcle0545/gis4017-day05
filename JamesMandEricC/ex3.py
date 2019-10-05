def is_point_on_line(x, y, m, b):

    if y == m *x + b:
        return True
    elif y != m*x + b:
        return False