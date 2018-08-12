import numpy as np
import pandas as pd
import bdateutil as bd
import datetime as dt
import calendar
from calendar_kb import Calendar_kb

if __name__ == '__main__':
    o_test_calendar=Calendar_kb(today=dt.date(2018,6,25),
                                maturity_date=(2018,9,25),day_convention='Actual/365')

    v_dates=o_test_calendar.move_dates_fun(shift=5,period='days')
    splited=o_test_calendar.split_year_equal(27)

    print('The end of the programm')