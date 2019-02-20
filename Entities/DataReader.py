# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:49:47 2017

@author: Archit
"""

from Entities.DataRow import DataRow
from Entities.Agent import Agent
from Entities.Claim import Claim
from Entities.Customer import Customer
from Entities.Doctor import Doctor
from Entities.Event import Event
from Entities.Hospital import Hospital
from Entities.Illness import Illness
from Entities.Policy import Policy
from Entities.Surgery import Surgery
from Entities.Visitation import Visitation

import pandas as pd

class DataReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read(self, sheet):
        dataRows = []
        df = pd.read_excel(self.filename, sheetname=sheet)
        
        for i in df.index:
            
            policy = Policy()
            policy.number = str(df['policy_no'][i])
            policy.issue_date = df['po_issue_date'][i].date()
            policy.premium_method = df['PremiumPaidmethod'][i]
            policy.medical_exam = df['medicalExam_required'][i]
            policy.decision = df['underwriting_decision'][i]
            policy.channel_code = df['channel_code'][i]
            
            dt = df['lapse_date'][i]
            policy.lapsed_date = None if pd.isnull(dt) else dt.date()
            policy.is_lapsed = not pd.isnull(dt)
            
            dt = df['reinstatment_date'][i]
            policy.reinstate_date = None if pd.isnull(dt) else dt.date()
            policy.is_reinstated = not pd.isnull(dt)
            
            dt = df['autopaiddate'][i]
            policy.autopaid_date = None if pd.isnull(dt) else dt.date()
            policy.is_autopaid = not pd.isnull(dt)
            
            policy.inforce_year = str(df['policyInforce_year'][i])
            policy.premium_frequency = str(df['PremiumPaidFrequencyPeryear'][i])
            policy.face_amount = df['face_amt'][i]
            policy.total_premium = df['Total_prem'][i]
            
            claim = Claim()
            claim.receipt_no = str(df['claim_rece_no'][i])
            claim.claim_no = str(df['claim_no'][i])
            claim.app_date = df['Claimappl_date'][i].date()
            claim.start_date = df['claim_date_start'][i].date()
            claim.end_date = df['claim_date_end'][i].date()
            claim.benf_days = df['claim_benef_days'][i]
            claim.amount_paid = df['amount'][i]
            claim.process_date = df['process_date'][i].date()
            
            dt = df['docter_proof_date'][i]
            claim.doctor_proof_date = None if pd.isnull(dt) else dt.date()
            claim.have_proof = not pd.isnull(dt)
            
            event = Event()
            event.date = df['event_date'][i].date()
            event.zip = df['zip'][i]
            event.type = str(df['event_type'][i])
            
            customer = Customer()
            customer.ID = str(df['insuredID'][i])
            s = df['Insured_sex'][i]
            customer.sex = None if pd.isnull(s) else str(s)
            customer.age = df['Insured_age'][i]
            s = df['marriage'][i]
            customer.marriage = None if pd.isnull(s) else str(s)
            s = df['education'][i]
            customer.education = None if pd.isnull(s) else str(s)
            s = df['occupation_class'][i]
            customer.occupation =  None if pd.isnull(s) else str(s)
            
            agent = Agent()
            agent.ID = df['agentid'][i]
            agent.officeID = df['agentin_center'][i]
            
            visitation = Visitation()
            visitation.reason = str(df['visit reasons_type'][i])
            visitation.urgency = str(df['ride_type'][i])
            
            hospital = Hospital()
            hospital.ID = str(df['hospital_num'][i])
            hospital.type = df['hosp_class'][i]
            hospital.dept1 = str(df['hospital_dept_1'][i])
            s = df['hospital_dept_2'][i]
            hospital.dept2 = None if pd.isnull(s) else str(s)
            
            surgery = Surgery()
            s = df['surgery_code (Insurer)'][i]
            surgery.code = None if pd.isnull(s) else str(s)
            surgery.date = df['surgery_date'][i].date()
            s = df['major_Surgery'][i]
            surgery.number_of_major_surgery = 0 if pd.isnull(s) else s
            surgery.start_date = df['surgey_date_start'][i].date()
            surgery.end_date = df['surgery_date_end'][i].date()
            
            doctor = Doctor()
            doctor.ID = df['doctor_num'][i]
            
            illness = Illness()
            illness.code = str(df['diag_code'][i])
            
            dataRow = DataRow()
            dataRow.id = i+1
            dataRow.agent = agent
            dataRow.claim = claim
            dataRow.customer = customer
            dataRow.doctor = doctor
            dataRow.event = event
            dataRow.hospital = hospital
            dataRow.illness = illness
            dataRow.policy = policy
            dataRow.surgery = surgery
            dataRow.visitation = visitation
            
            dataRows.append(dataRow)
        
        return dataRows
  


    
    
    

        

