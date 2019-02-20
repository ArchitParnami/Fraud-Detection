# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 16:35:07 2017

@author: Archit
"""

class Cluster:
    def __init__(self):
        self.data = []
        self.label = None
        self.left_child = None
        self.right_child = None
    
class ClusterSimilarityCalculator:
        def __init__(self, linkage):
            
            if linkage.lower() == "single":
                self.similarity = self.__find_max_similarity
            
        
        def calculate(self, cluster_1, cluster_2):
            return self.similarity(cluster_1, cluster_2)
        
        def __find_max_similarity(self, cluster_1, cluster_2):
            maximum = float('-inf')
            for x1 in cluster_1.data:
                for x2 in cluster_2.data:
                    d = x1.similarity(x2)
                    if d > maximum:
                        maximum = d
            return maximum
                


class HierarchialClustering:
    def __init__(self, linkage='single'):
        self.X = []
        self.Z = []
        self.clusters = []
        self.similarityCalcualtor = ClusterSimilarityCalculator(linkage)
        
        
    def fit(self, X):
        self.X = X
        self.__form_clusters()
        self.__start_clustering()
        return self.Z
     

           
    def __form_clusters(self):
        n = len(self.X)
        for i in range(n):
            cluster = Cluster()
            cluster.data = [self.X[i]]
            cluster.label = i
            cluster.left_child = None
            cluster.right_child = None
            self.clusters.append(cluster)
            
    def __start_clustering(self):
        count = len(self.clusters)
        while(len(self.clusters) > 1):
            c1, c2, similarity_score = self.__find_most_similar()
            c = Cluster()
            c.data = c1.data + c2.data
            c.left_child = c1
            c.right_child = c2
            c.label = count
            self.clusters.remove(c1)
            self.clusters.remove(c2)
            self.clusters.append(c)
            count += 1
            z = [c1.label, c2.label, 1-similarity_score, len(c.data)]
            self.Z.append(z)
    
    def __find_most_similar(self):
        max_similarity = float('-inf') 
        closest_pair = None
        n = len(self.clusters)
        for i in range(n):
            for j in range(i+1, n):
                c1 = self.clusters[i]
                c2 = self.clusters[j]
                score = self.similarityCalcualtor.calculate(c1, c2)
                if score > max_similarity:
                    max_similarity = score
                    closest_pair = (c1, c2, score)
                    
        return closest_pair
    
    
    def root(self):
        if len(self.clusters) == 1:
            return self.clusters[0]
                        