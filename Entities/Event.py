# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:09:55 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Event(SimilarityCalculator):
    def __init__(self):
        self.date = None
        self.zip = None
        self.type = None
        
    
    def similarity(self, other):
        if not isinstance(other, Event):
            return 0
        
        duration = self.date.month - other.date.month
        s1 = self.distance_score(duration)
        s2 = self.manhattan_score(self.zip, other.zip)
        s3 = self.equality_score(self.type, other.type)
        
        weights = [1/3] * 3
        scores = [s1, s2, s3]
        
        return self.weighted_score(weights, scores)