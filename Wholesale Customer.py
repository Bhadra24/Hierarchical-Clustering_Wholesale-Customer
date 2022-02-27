import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('D:/M V RAO/Data Science Course/7.My projects/Hierarchical Clustering/Wholesale customers data.csv') 

#There are multiple product categories – Fresh, Milk, Grocery, etc. The values represent the number of units purchased by 
#each client for each product. Our aim is to make clusters from this data that can segment similar clients together. 

#Premilinary Analysis
data.head()
data.info()
data.describe()
data.isnull().sum()
data.isna().sum()
data.nunique()
data.columns

# Normalization function 
from sklearn.preprocessing import normalize
data_scaled=normalize(data)
data_scaled=pd.DataFrame(data_scaled,columns=data.columns)
data_scaled.head()

#Model Building-Dendogram
# Using the dendrogram to find the optimal number of clusters
import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10,7))
plt.title('Dendograms')
dend=shc.dendrogram(shc.linkage(data_scaled, method='ward'))
#The vertical line with maximum distance is the blue line and hence we can decide a threshold of 6 and cut the dendrogram:
plt.figure(figsize=(10,7))
plt.title('Dendograms')
dend=shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.axhline(y=6, color='r', linestyle='--')

##Clustering##
from sklearn.cluster import AgglomerativeClustering
cluster=AgglomerativeClustering(n_clusters=2,linkage='ward',affinity='euclidean')
cluster.fit_predict(data_scaled)
#We can see the values of 0s and 1s in the output since we defined 2 clusters. 
#0 represents the points that belong to the first cluster and 1 represents points in the second cluster.

# Visualising the clusters
plt.figure(figsize=(10, 7))  
plt.scatter(data_scaled['Milk'], data_scaled['Grocery'], c=cluster.labels_) 
