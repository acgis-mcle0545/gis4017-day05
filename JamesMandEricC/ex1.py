def main():
    """main()"""

def get_feature_type(feature_code):

    if feature_code == 1:
        return 'POINT'
    if feature_code == 2:
        return 'POLYLINE'
    if feature_code == 3:
        return 'POLYGON'

if __name__ == '__main__':
   main()
