# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:11:17 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Hospital(SimilarityCalculator):
    def __init__(self):
        self.ID = None
        self.dept1 = None
        self.dept2 = None
        self.type = None
    
    
    def similarity(self, other):
        #features: [ID, dept1, dept2, type]
        if not isinstance(other, Hospital):
            return 0
        
        weights = [0.25,0.25,0.25,0.25]
        
        ID_score = self.equality_score(self.ID, other.ID)
        dept1_score = self.equality_score(self.dept1, other.dept1)
        dept2_score = self.equality_score(self.dept2, other.dept2)
        type_score = self.manhattan_score(self.type, other.type)
        
        scores = [ID_score, dept1_score, dept2_score, type_score]
        
        return self.weighted_score(weights, scores)
        
        