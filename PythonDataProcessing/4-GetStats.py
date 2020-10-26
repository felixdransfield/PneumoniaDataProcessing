import pandas as pd
from Processing.Utils import get_distribution_percentages, get_distribution_counts

def main():
    aggregate_series = pd.read_csv("Data/TimeSeriesAggregated.csv")
    cohort = pd.read_csv("Data/DemographicsOutcomesCleaned.csv")
    unique_admissions = set(aggregate_series['PatientID'])
    print(" number of records: ", aggregate_series.shape[0], "unique admissions: ", len(unique_admissions))
    cohort_subset = cohort.loc[cohort['hadm_id'].isin(unique_admissions)]
    print(" Female percentages ", get_distribution_percentages(cohort_subset['gender']))
    print(" Female counts ", get_distribution_counts(cohort_subset['gender']))
    print(" Age stats", cohort_subset['age'].describe())

    death_columns = cohort_subset['deathperiod'].copy()
    death_columns_bool = [0 if x =='-1'  else 1 for x in death_columns ]
    print(" Death perentages: ", get_distribution_percentages(death_columns_bool))
    print(" Death counts: ", get_distribution_counts(death_columns_bool))

    print(cohort.columns)
    death_periods_int = [0 if x =='-1' else int(x.split('da')[0]) for x in death_columns]
    print(death_periods_int)
    death_periods_int = [x for x in death_periods_int if x > 0]
    print(death_periods_int)

    print(" Death periods stats", pd.Series(death_periods_int).describe())

    itu_columns = cohort_subset['ituperiod'].copy()

    print(cohort.columns)
    itu_periods_int = [0 if x =='-1' else int(x.split('da')[0]) for x in itu_columns]
    print(itu_periods_int)
    itu_periods_int = [x for x in itu_periods_int if x > 0]
    print(itu_periods_int)
    print(" ITU periods stats", pd.Series(itu_periods_int).describe())



if __name__ == "__main__" :
    main()