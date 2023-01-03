import math
import datetime as dt
from workadays import workdays as wd

YEAR_WORKDAYS_BR = 252


def get_br_work_days(startdate, enddate):
    # return total workdays between two dates
    return wd.networkdays( startdate, enddate, country='BR')

def get_ltn_price( workdays, tax_rate ):
    price = 1000.00 / math.pow(1 + tax_rate/100, workdays / YEAR_WORKDAYS_BR )

    return trunc_price( price )

def get_ltn_future( price, tax_rate, workdays):
    future = price * math.pow( 1 + tax_rate/100, workdays / YEAR_WORKDAYS_BR)
    
    return trunc_price ( future )

def get_ltn_tax(startdate, enddate, price):
    workdays = get_br_work_days( startdate, enddate )
    rate = math.pow( 1000.0 / price, YEAR_WORKDAYS_BR / workdays ) - 1

    return rate

def get_ltn_price_from_tax( startdate, enddate, tax_rate):
    workdays = get_br_work_days( startdate, enddate )
    price = 1000.0 / math.pow( 1 + tax_rate / 100.0, workdays / YEAR_WORKDAYS_BR )

    return trunc_price( price )

def trunc_price( price ):
    # based on calculation metodology of brazilian federal public securities
    return math.ceil( price * 1e6) / 1e6

def trunc_tax_rate( tax_rate ):
    # based on calculation metodology of brazilian federal public securities
    return math.ceil( tax_rate * 1e4) / 1e4