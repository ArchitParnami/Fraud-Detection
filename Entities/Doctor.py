# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 14:48:54 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Doctor(SimilarityCalculator):
    def __init__(self):
        self.ID = None
    
    def similarity(self, other):
        if not isinstance(other, Doctor):
            return 0
        return self.equality_score(self.ID, other.ID)
    
