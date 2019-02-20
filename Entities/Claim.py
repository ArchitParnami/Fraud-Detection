# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:21:29 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Claim(SimilarityCalculator):
    def __init__(self):
        self.receipt_no = None
        self.claim_no = None
        self.app_date = None
        self.start_date = None
        self.end_date = None
        self.benf_days = None
        self.amount_paid = None
        self.process_date = None
        self.doctor_proof_date = None
        self.have_proof = None
        
    def similarity(self, other):
        if not isinstance(other, Claim):
            return 0.0
        
        duration = (self.end_date - self.start_date).days + 1
        duration_other = (other.end_date - other.start_date).days + 1
        s1 = self.manhattan_score(duration, duration_other)
        s2 = self.manhattan_score(self.amount_paid/1000, other.amount_paid/1000)
        
#        #how many days it took to get doctors approval from start date
#        d = (self.start_date - self.doctor_proof_date + 1)
#        d_other = (other.start_date - other.doctor_proof_date + 1)
#        s3 = self.manhattan_score(d, d_other)
        
        #temporal similarity
        diff_months = self.app_date.month - other.app_date.month
        s4 = self.distance_score(diff_months)
        
        weights = [1/3] * 3
        scores = [s1, s2, s4]
        
        return self.weighted_score(weights, scores)
        
        