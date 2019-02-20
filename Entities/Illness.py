# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:30:46 2017

@author: Archit
"""

from Entities.SimilarityCalculator import SimilarityCalculator

class Illness(SimilarityCalculator):
    def __init__(self):
        self.code = None
    
    def __code_similarity(self, code1, code2):
        type1 = code1[0]
        type2 = code2[0]
        score = None
        
        if type1 != type2:
            score = 0.0
        else:
            if code1 == code2:
                score = 1.0
            else:
                score = 0.5
        return score
            
        
    
    def similarity(self, other):
        if not isinstance(other, Illness):
            return 0
        
        return self.__code_similarity(self.code, other.code)
        