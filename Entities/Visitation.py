# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:33:20 2017

@author: Archit
"""


from Entities.SimilarityCalculator import SimilarityCalculator

class Visitation(SimilarityCalculator):
    def __init__(self):
        self.reason = None
        self.urgency = None
    
    def similarity(self, other):
        if not isinstance(other, Visitation):
            return 0

        s1 = self.equality_score(self.reason, other.reason)
        s2 = self.equality_score(self.urgency, other.urgency)
        
        weights = [1/2] * 2
        scores = [s1, s2]
        
        return self.weighted_score(weights, scores)