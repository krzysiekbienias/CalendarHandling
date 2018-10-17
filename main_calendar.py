import numpy as np
import pandas as pd
from pandas.tseries.offsets import *
import bdateutil as bd
import datetime as dt
import calendar
from calendar_kb import CashflowsCalendar,ScenariosCalendar

if __name__ == '__main__':
    o_scenario_calendar=ScenariosCalendar(today='2018-08-20',day_convention='Actual/365',maturity_date='2018-11-20')

    print('The end of the programm')