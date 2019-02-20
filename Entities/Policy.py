# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:09:44 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Policy(SimilarityCalculator):
    def __init__(self):
        self.number = None
        self.issue_date = None
        self.premium_method = None
        self.medical_exam = None
        self.decision = None
        self.channel_code = None
        self.is_lapsed = None
        self.lapsed_date = None
        self.is_reinstated = None
        self.reinstate_date = None
        self.is_autopaid = None
        self.autopaid_date = None
        self.inforce_year = None
        self.premium_frequency = None
        self.face_amount = None
        self.total_premium = None
        
    def similarity(self, other):
        if not isinstance(other, Policy):
            return 0

        d = self.issue_date.month - other.issue_date.month
        s1 = self.distance_score(d)
        s2 = self.equality_score(self.premium_method, other.premium_method)
        s3 = self.equality_score(self.medical_exam, other.medical_exam)
        s4 = self.equality_score(self.decision, other.decision)
        s5 = self.equality_score(self.channel_code, other.channel_code)
        s6 = self.equality_score(self.is_lapsed, other.is_lapsed)
        s7 = self.equality_score(self.is_reinstated, other.is_reinstated)
        s8 = self.equality_score(self.is_autopaid, other.is_autopaid)
        s9 = self.equality_score(self.inforce_year, other.inforce_year)
        s10 = self.equality_score(self.premium_frequency, other.premium_frequency)
        s11 = self.manhattan_score(self.face_amount/10000, other.face_amount/10000)
        s12 = self.manhattan_score(self.total_premium, other.total_premium)
        
        scores = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12]
        weights = [1/12] * 12
        
        return self.weighted_score(weights, scores)
        