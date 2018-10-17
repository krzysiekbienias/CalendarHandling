import numpy as np
import pandas as pd
import bdateutil as bd
import datetime as dt
import calendar
from pandas.tseries.offsets import *

class CashflowsCalendar:
    def __init__(self, today, day_convention,maturity_date=None):
        self.today = today
        self.day_convention = day_convention
        self.maturity_date = maturity_date

    def get_time_step_fun(self, data_frame):
        return data_frame['Data_maturity']  # it depends from column names in excel that contains maturity data.

    def year_fraction_two_dates_fun(self):

        if self.day_convention == 'Actual/365':
                delta = (self.maturity_date.toordinal()-self.today.toordinal())/365
        if self.day_convention == 'Actual/360':
                delta = (self.maturity_date.toordinal()-self.today.toordinal())/360
        if self.day_convention == '30/360':
                delta = (max(30-self.today.day, 0)+min(self.maturity_date.day, 30)+360*(self.maturity_date.year-
                CashflowsCalendar.today.year)+30*(self.maturity_date.month-self.month-1))/360
        return delta

    def days_difference_fun(self):  # ONLY TWO CONVENTIONS
        if self.day_convention == 'Actual/365':
            self.delta = (self.maturity_date.toordinal() - self.today.toordinal())
        if self.day_convention == 'Actual/360':
            self.delta = (self.maturity_date.toordinal() - self.today.toordinal())

        return self

    def year_fraction_fun(self, shift, period):
        if period == 'days':
            next_dates = self.today + bd.relativedelta(days=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        if period == 'months':
            next_dates = self.today + bd.relativedelta(months=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        if period == 'years':
            next_dates = self.today + bd.relativedelta(years=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        if self.day_convention == 'Actual/365':
            delta = (next_dates.toordinal() - self.today.toordinal()) / 365
        if self.day_convention == 'Actual/360':
            delta = (next_dates.toordinal() - self.today.toordinal()) / 360
        if self.day_convention == '30/360':
            delta = (max(30 - self.today.day, 0) + min(next_dates.day, 30) + 360 * (
                    next_dates.year - self.today.year) + 30 * (
                             next_dates.month - self.today.month - 1)) / 360
        return delta

    def move_dates_fun(self, shift, period):
        if period == 'days':
            next_dates = self.today + bd.relativedelta(days=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Friday':
                next_dates = next_dates + bd.relativedelta(days=+3)

        if period == 'months':
            next_dates = self.today + bd.relativedelta(months=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        if period == 'years':
            next_dates = self.today + bd.relativedelta(years=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        return next_dates

    def days_from_today(self,period,shift):
        if period == 'days':
            next_dates = self.today + bd.relativedelta(days=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)#TODO tak odliczanie od piatku tez nie dziala trzeba zrobic jak w mainie w przypadku days

        if period == 'months':
            next_dates = self.today + bd.relativedelta(months=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)
        if period == 'years':
            next_dates = self.today + bd.relativedelta(years=+shift)
            check = calendar.day_name[next_dates.weekday()]
            if check == 'Sunday':
                next_dates = next_dates + bd.relativedelta(days=+1)
            if check == 'Saturday':
                next_dates = next_dates + bd.relativedelta(days=+2)

        delta = next_dates.toordinal() - self.today.toordinal()
        return delta

    def year_fraction_between_two_dates(self, data_frame):
        pillars = self.get_time_step_fun(data_frame)
        delta = np.zeros(len(pillars))
        for i in range(1, len(pillars)):
            if self.day_convention == 'Actual/365':
                delta[i] = (pillars[i].toordinal() - pillars[i - 1].toordinal()) / 365
            if self.day_convention == 'Actual/360':
                delta[i] = (pillars[i].toordinal() - pillars[i - 1].toordinal()) / 360
            if self.day_convention == '30/360':
                delta[i] = (max(30 - pillars[i - 1].day, 0) + min(pillars[i].day, 30) + 360 * (
                        pillars[i].year - pillars[i - 1].year) + 30 * (
                                 pillars[i - 1].month - pillars[i].month - 1)) / 360
        return delta[1:]

    def year_fraction_sequence_from_fixed_date(self, data_frame):
        pillars = self.get_time_step_fun(data_frame)
        delta = np.zeros(len(pillars))
        for i in range(0, len(pillars)):
            if self.day_convention == 'Actual/365':
                delta[i] = (pillars[i].toordinal() - self.today.toordinal()) / 365
            if self.day_convention == 'Actual/360':
                delta[i] = (pillars[i].toordinal() - self.today.toordinal()) / 360
            if self.day_convention == '30/360':
                delta[i] = (max(30 - self.today.day, 0) + min(self.today.day, 30) + 360 * (
                        self.today.year - self.today.year) + 30 * (
                        self.today.month - self.today.month - 1)) / 360
        return delta

    def split_year_equal(self,parts):
        return int(round(365/parts,0))


class ScenariosCalendar:
    def __init__(self, today, day_convention,lag, maturity_date=None,live_of_contract=None):
        self._stoday=today #only convention that this variable is private,_sxxx=string,sexxx=series
        self._sday_convention=day_convention
        self._smaturity_date=maturity_date
        self._lag=lag
        self.live_of_contract=live_of_contract
        self.spot_date=self.get_spot_date()
        self.se_date_series=self.get_date_series()
        self.l_increments=self.get_increments()

    def get_spot_date(self):#TODO if days=0 spot_date=today, add that
        if (self._lag!=0):
            spot_date=self._stoday+bd.relativedelta(days=+self._lag)
        else:
            spot_date = self._stoday
        return spot_date

    def year_fraction_two_dates_fun(self):
        if self.day_convention == 'Actual/365':
                delta = (self.maturity_date.toordinal()-self.spot_date.toordinal())/365
        if self.day_convention == 'Actual/360':
                delta = (self.maturity_date.toordinal()-self.today.toordinal())/360
        if self.day_convention == '30/360':
                delta = (max(30-self.today.day, 0)+min(self.maturity_date.day, 30)+360*(self.maturity_date.year-
                CashflowsCalendar.today.year)+30*(self.maturity_date.month-self.month-1))/360
        return delta

    def get_date_series(self):
        dates = pd.date_range(self.spot_date,self._smaturity_date, freq='B')
        se_dates = pd.Series(dates)
        return se_dates

    def get_increments(self):
        time_index=pd.date_range(self.spot_date,self._smaturity_date, freq='B')#time_index object
        two_consequitive=[(time_index[i]-time_index[i-1]) for i in range(1,len(time_index))]
        dt=[two_consequitive[i].days/365 for i in range(len(two_consequitive))]
        return dt




