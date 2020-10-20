import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import math

def clean_vitals(vitals):
    timeseries_columns = list(set(vitals['vitalid']))
    timeseries_columns.append('icustay_id')
    timeseries = pd.DataFrame(columns = timeseries_columns)
    return vitals

def clean_cohort(cohort):
    cohort.drop(['dob', 'subject_id'], inplace=True, axis=1)
    cohort['admittime'] = [x.replace(':00 ', '') for x in cohort['admittime']]
    cohort['gender'] = np.where(cohort['gender'] == "F", 1, 0)

    cohort['admittime'] = [datetime.strptime(x, '%d/%m/%y %H:%M') for x in cohort['admittime']]
    cohort['deathtime'] = ['' if str(x) =="nan" else datetime.strptime(x, '%d/%m/%y %H:%M') for x in cohort['deathtime'] ]

    death_period = []
    death_period_int = []

    mortality_3days = []
    mortality_5days = []
    mortality_7days = []
    mortality_14days = []
    mortality_30days = []
    for index, row in cohort.iterrows():
        if pd.isnull(row['deathtime']):
            death_period.append(-1)
            mortality_3days.append(0)
            mortality_5days.append(0)
            mortality_7days.append(0)
            mortality_14days.append(0)
            mortality_30days.append(0)
        else:
            death_range = row['deathtime'] - row['admittime']
            death_range_int = int((str(death_range)).split('da')[0])
            death_period_int.append(death_range_int)
            death_period.append(death_range)

            if (death_range <= timedelta(days=3)) :
                mortality_3days.append(1)
                mortality_5days.append(1)
                mortality_7days.append(1)
                mortality_14days.append(1)
                mortality_30days.append(1)
            elif (death_range <= timedelta(days=5)) :
                mortality_3days.append(0)
                mortality_5days.append(1)
                mortality_7days.append(1)
                mortality_14days.append(1)
                mortality_30days.append(1)
            elif (death_range <= timedelta(days=7)) :
                mortality_3days.append(0)
                mortality_5days.append(0)
                mortality_7days.append(1)
                mortality_14days.append(1)
                mortality_30days.append(1)
            elif (death_range <= timedelta(days=14)) :
                mortality_3days.append(0)
                mortality_5days.append(0)
                mortality_7days.append(0)
                mortality_14days.append(1)
                mortality_30days.append(1)
            elif (death_range <= timedelta(days=30)):
                mortality_3days.append(0)
                mortality_5days.append(0)
                mortality_7days.append(0)
                mortality_14days.append(0)
                mortality_30days.append(1)
            else:
                mortality_3days.append(0)
                mortality_5days.append(0)
                mortality_7days.append(0)
                mortality_14days.append(0)
                mortality_30days.append(0)


    cohort['deathperiod'] = death_period
    cohort['3DM'] = mortality_3days
    cohort['5DM'] = mortality_5days
    cohort['7DM'] = mortality_7days
    cohort['14DM'] = mortality_14days
    cohort['30DM'] = mortality_30days

    return cohort

def removeDateSuffix(df):
    dates = []
    for s in df:
        parts = s.split()
        parts[1] = parts[1].strip("stndrh") # remove 'st', 'nd', 'rd', ...
        dates.append(" ".join(parts))

    return dates

def updateDate(df):
    date_output_format = "%Y-%m-%d"

    dates = []
    for t in df:
        if t == '' or pd.isnull(t) :
            d = np.nan
        elif "-" in t :
            fmt = "%y-%m-%d"
            d = pd.to_datetime(t, format=fmt, exact=False, utc=True)
        elif "/" in t :
            fmt = "%d/%m/%y"
            d = pd.to_datetime(t, format=fmt, exact=False)
        else :
            fmt = None
            d = pd.to_datetime(t, format=fmt, exact=False)
        if pd.isnull(d):
            dates.append(np.nan)
        else:
            dates.append(d.strftime(date_output_format))
    return dates

def updateDateTime(df):
    date_output_format = "%Y-%m-%d %H:%M:%S"
    dates = []
    for t in df:
        if "-" in t :
            fmt = "%y-%m-%d %H:%M"
            d = pd.to_datetime(t, format=fmt, exact=False, utc=True)
        elif "/" in t :
            fmt = "%d/%m/%y %H:%M"
            d = pd.to_datetime(t, format=fmt, exact=False)
        else :
            fmt = None
            d = pd.to_datetime(t, format=fmt, exact=False)
        dates.append(d.strftime(date_output_format))
    return dates
