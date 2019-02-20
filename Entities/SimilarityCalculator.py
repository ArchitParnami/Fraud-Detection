# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:05:10 2017

@author: Archit
"""

from abc import ABC, abstractmethod


class SimilarityCalculator(ABC):
    
    @abstractmethod
    def similarity(self, obj):
        pass
    
    def equality_score(self, value1, value2):
        return 1.0 if value1 == value2 else 0
    
    def manhattan_score(self, value1, value2):
        diff = abs(value1 - value2)
        score = 1.0 / (diff + 1.0)
        return score
    
    def weighted_score(self, weights, scores):
        n = len(weights)
        score = 0.0
        for i in range(n):
            score += weights[i] * scores[i]
        return score
    
    def distance_score(self, distance):
        return 1 / (abs(distance) + 1.0)