import numpy as np
import pandas as pd
import bdateutil as bd
import datetime as dt
import calendar

class Calendar_kb:
    def __init__(self, today, maturity_date, day_convention):
        self.today = today
        self.maturity_date = maturity_date
        self.day_convention = day_convention

    def get_time_step_fun(self, data_frame):
        return data_frame['Data_maturity']  # it depends from column names in excel that contains maturity data.

    def year_fraction_two_dates_fun(self):

        if self.day_convention == 'Actual/365':
                delta = (self.maturity_date.toordinal()-self.today.toordinal())/365
        if self.day_convention == 'Actual/360':
                delta = (self.maturity_date.toordinal()-self.today.toordinal())/360
        if self.day_convention == '30/360':
                delta = (max(30-self.today.day, 0)+min(self.maturity_date.day, 30)+360*(self.maturity_date.year-
                Calendar_kb.today.year)+30*(self.maturity_date.month-self.month-1))/360
        return delta

    def days_difference_fun(self):  # ONLY TWO CONVENTIONS
        if self.day_convention == 'Actual/365':
            delta = (self.maturity_date.toordinal() - self.today.toordinal())
        if self.day_convention == 'Actual/360':
            delta = (self.maturity_date.toordinal() - self.today.toordinal())
        return delta

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
        return next_dates

    def days_from_today(self,period,shift):
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



if __name__ == '__main__':
    o_test_calendar=Calendar_kb(today=dt.date(2018,6,25),
                                maturity_date=(2018,9,25),day_convention='Actual/365')

    v_dates=o_test_calendar.move_dates_fun(shift=5,period='days')

    print('The end of the programm')


