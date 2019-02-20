# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:37:08 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class DataRow(SimilarityCalculator):
    def __init__(self):
        self.id = None
        self.policy = None
        self.claim = None
        self.event = None
        self.customer = None
        self.agent = None
        self.visitation = None 
        self.hospital = None
        self.surgery = None
        self.doctor = None
        self.illness = None
    
    def similarity(self, other):
        
        if not isinstance(other, DataRow):
            return 0
           
        s1 = self.policy.similarity(other.policy)
        s2 = self.claim.similarity(other.claim)
        s3 = self.event.similarity(other.event)
        s4 = self.customer.similarity(other.customer)
        s5 = self.agent.similarity(other.agent)
        s6 = self.visitation.similarity(other.visitation)
        s7 = self.hospital.similarity(other.hospital)
        s8 = self.surgery.similarity(other.surgery)
        s9 = self.doctor.similarity(other.doctor)
        s10 = self.illness.similarity(other.illness)
        
        scores = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
        weights = [0.1] * 10    
        return self.weighted_score(weights, scores)
    