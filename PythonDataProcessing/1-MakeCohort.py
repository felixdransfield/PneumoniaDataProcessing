import pandas as pd
from Cohort.Cohort import Cohort
from Processing.Utils import convert_to_datetime

from Processing.Clean import clean_cohort, clean_vitals
from Processing.Serialisation import jsonDump


def main():
    #1. extract only first icu stay
    #vitals_data = pd.read_csv("Data/TimeSeries.csv")

    #hadm_ids = set(vitals_data['hadm_id'])

    #vitals_data = vitals_data[~vitals_data['vitalid'].isin(['MeanBP2', 'SysBP2', 'DiasBP2'])]
    #vitals_data_subset = pd.DataFrame(columns = vitals_data.columns)
    #for idx in hadm_ids:
     #   admission_df = vitals_data.loc[vitals_data['hadm_id'] == idx]
     #   first_icustay = (admission_df['icustay_id']).iloc[0]
     #   icustay_df = vitals_data.loc[vitals_data['icustay_id'] == first_icustay]
     #   vitals_data_subset = vitals_data_subset.append(icustay_df, ignore_index=True)

    #num_admissions_final = len(set(vitals_data_subset['hadm_id']))
    #print("SHAPE OF THE FINAL DF: ", vitals_data_subset.shape, "number of admissions in it: ", num_admissions_final)
    #vitals_data_subset.to_csv("Data/vitals_final.csv", index=False)


    vitals = pd.read_csv("Data/vitals_final.csv")
    cohort_data = pd.read_csv("Data/DemographicsOutcomes.csv")
    #obtain only patients whose time-series we have
    cohort_data = cohort_data[cohort_data['hadm_id'].isin(vitals['hadm_id'])]
    #recode males = 0, females = 1

    cohort_data = clean_cohort(cohort_data)
    #print(get_distribution_percentages(cohort_data['30DM']))
    cohort_data.to_csv("Data/DemographicsOutcomesCleaned.csv", index=False)

    vitals_data = clean_vitals(vitals)

    cohort = Cohort(cohort_data, 'hadm_id', "PneumoniamMIMIC")


    admission_ids = set(cohort_data.hadm_id)

    for idx in admission_ids :
        patientAdmissionDate = cohort_data.loc[cohort_data['hadm_id'] == idx].loc[:, 'admittime'].values[0]
        #print(" admission date before conversion: ", patientAdmissionDate, " and class: ", type(patientAdmissionDate))
        #patientAdmissionDate = datetime.strptime(str(patientAdmissionDate), '%d/%m/%y %H:%M')
        patientAdmissionDate = convert_to_datetime(patientAdmissionDate)

        vitals_for_patient = vitals_data.loc[vitals_data['hadm_id'] == idx]
        vitals_for_patient.drop(['subject_id', 'icustay_id'], axis=1, inplace=True)
        vitals_for_patient.columns = ['hadm_id', 'time', 'value', 'valuenum', 'valueuom', 'vitalid']

        vitals_for_patient['time'] = pd.to_datetime(vitals_for_patient['time'])
        vitals_for_patient['time'] = vitals_for_patient['time'].astype(str)

        if vitals_for_patient.shape[0]:
            cohort.addBloodObservations(idx, vitals_for_patient, patientAdmissionDate)

    jsonDump(cohort, "Data/Cohort.json")

if __name__ == "__main__":
    main()