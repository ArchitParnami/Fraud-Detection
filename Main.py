# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:29:08 2017

@author: Archit
"""

from Entities.DataReader import DataReader
from HierarchialClustering import HierarchialClustering
#from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
#from matplotlib import pyplot as plt
#import numpy as np

filename = "dataset.xlsx"
sheet = "sheet1"

dr = DataReader(filename)
dataRows = dr.read(sheet)

#def SimilarityMatrix(X):
#    N = len(X)
#    M = [ [0] * N for i in range(N)]
#    for i in range(N):
#        for j in range(N):
#            M[i][j] = 1-X[i].similarity(X[j])
#    return M
#    
#def plot_dendrogram(model, **kwargs):
#
#    # Children of hierarchical clustering
#    children = model.children_
#
#    # Distances between each pair of children
#    # Since we don't have this information, we can use a uniform one for plotting
#    distance = np.arange(children.shape[0])
#
#    # The number of observations contained in each cluster level
#    no_of_observations = np.arange(2, children.shape[0]+2)
#
#    # Create linkage matrix and then plot the dendrogram
#    linkage_matrix = np.column_stack([children, distance, no_of_observations]).astype(float)
#
#    # Plot the corresponding dendrogram
#    dendrogram(linkage_matrix, **kwargs)
    
#get rows with year 1995
X = [row for row in dataRows if row.policy.issue_date.year==1995]

#X = [row for row in dataRows if row.policy.issue_date.year == 2000]

Y = [row.id for row in X]

#M = SimilarityMatrix(X)

#perform clustering
H = HierarchialClustering()
Z = H.fit(X)

#H = AgglomerativeClustering(affinity='precomputed', linkage='average')
#H.fit(M)

d = dendrogram(Z, labels=Y,orientation='top')

#plot_dendrogram(H, labels=Y)
#plt.show()