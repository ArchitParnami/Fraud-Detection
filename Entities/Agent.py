# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 18:06:54 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Agent(SimilarityCalculator):
    def __init__(self):
        self.ID = None
        self.officeID = None
    
    def similarity(self, other):
        if not isinstance(other, Agent):
            return 0.0
        
        weights = [0.5, 0.5]
        ID_score = self.equality_score(self.ID, other.ID)
        office_score = self.equality_score(self.officeID, other.officeID)
        scores = [ID_score, office_score]
        return self.weighted_score(weights, scores)

