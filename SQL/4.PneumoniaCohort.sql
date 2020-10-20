set search_path to mimicfull; 
drop table if exists pneumonia.PneumoniaSeries cascade; 

set search_path to mimicfull; 
drop table if exists pneumonia.TimeSeries cascade; 

create table pneumonia.TimeSeries as
	select subject_id, hadm_id, icustay_id, time, value, valuenum, valueuom, vitalid from  pneumonia.vitalsfirstday
		where vitalid is not null and hadm_id in (select hadm_id from mimicfull.diagnoses_icd where icd9_code ='486'); 

update pneumonia.TimeSeries  
	SET
	valuenum = valuenum*0.45 where vitalid = 'Weightlb';
	

update pneumonia.TimeSeries  
	SET
	valuenum = ((valuenum - 32)*5/9) where valuenum > 50 and vitalid = 'Temperature';



drop table if exists pneumonia.DemographicsOutcomes
create table pneumonia.DemographicsOutcomes as
	select mimicfull.admissions.subject_id, 
		mimicfull.admissions.hadm_id,
		case when deathtime is not null then 
				deathtime	
			else null end as deathtime
		, 
		admittime
		,
		dischtime  - admittime as los
		, gender
		, date_part('year',age(dob,current_date) )as age
		, dob
			
	from mimicfull.admissions, mimicfull.patients

	where 
	
	mimicfull.admissions.subject_id = mimicfull.patients.subject_id and mimicfull.admissions.hadm_id in (select hadm_id from pneumonia.TimeSeries);




