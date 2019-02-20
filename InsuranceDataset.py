#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 03:09:03 2017

@author: archit
"""
from Entities.DataReader import DataReader

filename = "dataset.xlsx"
sheet = "sheet1"


class InsuranceDataset:
    def __init__(self):
        self.dataRows = []
        self.claims_per_year = []
        self.claims_per_agent = []
        self.claims_per_doctor = []
        self.years = []
        self.agents= []
        self.doctors = []
      
    def load(self):
        dr = DataReader(filename)
        self.dataRows = dr.read(sheet)
    

    def build_statistics(self):
        
        years = {}
        agents = {}
        doctors = {}
        
        for row in self.dataRows:
            
            x = row.policy.issue_date.year
            agent = row.agent.ID
            doctor = row.doctor.ID
            
            if x in years:
                years[x] += 1
            else:
                years[x] = 1
              
                
            if agent in agents:
                if x in agents[agent]:
                    agents[agent][x] += 1
                else:
                    agents[agent][x] = 1
            else:
                agents[agent] = {x:1}
            
            
            if doctor in doctors:
                if x in doctors[doctor]:
                    doctors[doctor][x] += 1
                else:
                    doctors[doctor][x] = 1
            else:
                doctors[doctor] = {x:1}
            
            
        
        self.years = sorted(years.keys())
        self.agents = sorted(agents.keys())
        self.doctors = sorted(doctors.keys())
        
        for year in self.years:
            self.claims_per_year.append(years[year])
        
        for agent in self.agents:
            claims = []
            for year in self.years:
                if year in agents[agent]:
                    n = agents[agent][year]
                else:
                    n = 0
                claims.append(n)
                    
            self.claims_per_agent.append(claims)

        for doctor in self.doctors:
            claims = []
            for year in self.years:
                if year in doctors[doctor]:
                    n = doctors[doctor][year]
                else:
                    n = 0
                claims.append(n)
                    
            self.claims_per_doctor.append(claims)
    
        