# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:05:18 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Surgery(SimilarityCalculator):
    def __init__(self):
        self.code = None
        self.date = None
        self.start_date = None
        self.end_date = None
        self.number_of_major_surgery = 0
        
    
    def similarity(self, other):
        #features
        #[code, duration, number_of_major_surgery]
        
        if not isinstance(other, Surgery):
            return 0
        
        weights = [0.5, 0.25, 0.25]
        
        code_score = self.equality_score(self.code, other.code)
    
        duration1 = (self.end_date - self.start_date).days + 1
        duration2 = (other.end_date - other.start_date).days + 1
        duration_score = self.manhattan_score(duration1, duration2)
        
        major_score = self.manhattan_score(self.number_of_major_surgery, other.number_of_major_surgery)
       
        scores = [code_score, duration_score, major_score]
      
        
        return self.weighted_score(weights, scores)
        
        