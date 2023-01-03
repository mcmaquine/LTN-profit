import ltn
import datetime as dt
import math

def main():
    print('Start LTN search')
    start = dt.date( 2020, 11, 17)
    end = dt.date(2021, 1, 1)

    print( ltn.get_ltn_price_from_tax(start, end, 1.97))


if __name__ == "__main__":
    #just to remenber: __name__ refers to this file name
    main()