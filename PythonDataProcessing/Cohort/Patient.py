import pandas as pd
from datetime import datetime, timedelta
from dateutil import parser
from Processing.Utils import convert_to_datetime
class Patient:
    def __init__(self, id, los,gender, age, m3, m5, m7, m14, m30,admitDate=None, deathDate=None,deathperiod=-1):

        self.Patient_id = id
        self.Age = age
        self.Gender = gender
        if not (pd.isnull(admitDate)):
            AdmitDate = convert_to_datetime(admitDate)
        if not (pd.isnull(deathDate)):
            DeathDate = convert_to_datetime(deathDate)

        if not (pd.isnull(deathDate)) and not (pd.isnull(admitDate)):
            self.deathRange = DeathDate- AdmitDate
        else:
            self.deathRange = -1
        self.AdmitDate = admitDate
        self.DeathDate = deathDate
        self.los = los
        self.M3 = m3
        self.M5 = m5
        self.M7 = m7
        self.M14 = m14
        self.M30 = m30
        self.observations = []

    def addObservations( self, observations ):
        for o in observations:
            self.observations.append(o)

    def printString( self ):
        print(" Patient: ", self.Patient_id, self.Age, self.Gender)

    def printObservationVolume( self ):
        print(" Patient: ", self.Patient_id," has: ", len(self.observations), "observations")

    def getNumberOfObservations( self ):
        return len(self.observations)

    def as_dict(self):
        patient_row = {'PatientID' : self.Patient_id,
                       'Age' : self.Age,
                       'Gender' : self.Gender,
                       'los': self.los,
                       'DeathPeriod' : self.deathRange,
                       'Mortality3Days': self.M3,
                       'Mortality5Days' : self.M5,
                       'Mortality7Days' : self.M7,
                       'Mortality14Days' : self.M14,
                       'Mortality30Days' : self.M30
                       }
        return patient_row