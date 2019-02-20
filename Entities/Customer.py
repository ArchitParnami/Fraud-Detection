# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:16:49 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Customer(SimilarityCalculator):
    def __init__(self):
        self.ID = None
        self.sex = None
        self.age = None
        self.marriage = None
        self.education = None
        self.occupation = None
        
    def similarity(self, other):
        if not isinstance(other, Customer):
            return 0
           
        s1 = self.equality_score(self.ID, other.ID)
        s2 = self.equality_score(self.sex, other.sex)
        s3 = self.equality_score(self.marriage, other.marriage)
        s4 = self.equality_score(self.education, other.education)
        s5 = self.equality_score(self.occupation, other.occupation)
        s6 = self.manhattan_score(self.age, other.age)
        
        weights = [1/6] * 6
        scores = [s1, s2, s3, s4, s5, s6]
        
        return self.weighted_score(weights, scores)