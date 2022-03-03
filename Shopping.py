#Import Libraries & Load dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#The problem that we are going to solve in this section is to segment customers into different groups based on their shopping trends.
customer_data=pd.read_csv('D:/M V RAO/Data Science Course/7.My projects/Hierarchical Clustering/Customer shopping_dataset.csv') 

#Preliminary Analysis/Explore Data
customer_data.head()
customer_data.info()
customer_data.describe()
customer_data.isnull().sum()
customer_data.isna().sum()
customer_data.nunique()
customer_data.columns
customer_data

#Data Preprocessing
#We can remove CustomerID column, Genre, and Age column. We will retain the Annual Income & Spending Score columns. 
#The Spending Score column signifies how often a person spends money in a mall on a scale of 1 to 100 with 100 being the highest spender.
data=customer_data.iloc[:,3:5].values

#Model Building
from scipy.cluster.hierarchy import linkage
z=linkage(data,method='complete',metric='euclidean')
import scipy.cluster.hierarchy as sch
sch.dendrogram(z,leaf_rotation=0.,leaf_font_size=8.)
#plt.axhline(y=85, color='r', linestyle='--')
plt.show

# =============================================================================
# #In the script above we import the hierarchy class of the scipy.cluster library as shc. The hierarchy class has a dendrogram 
# #method which takes the value returned by the linkage method of the same class. The linkage method takes the dataset and the 
# #method to minimize distances as parameters.
# =============================================================================

##Clustering##
from sklearn.cluster import AgglomerativeClustering
cluster=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean')
cluster.fit_predict(data)

#Visualization
plt.figure(figsize=(10, 7))
plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')

#Conclusion
# =============================================================================
# You can see the data points in the form of five clusters. The data points in the bottom right belong to the customers with 
# high salaries but low spending. These are the customers that spend their money carefully. Similarly, the customers at top right 
# (green data points), these are the customers with high salaries and high spending. These are the type of customers that 
# companies target. The customers in the middle (blue data points) are the ones with average income and average salaries. 
# The highest numbers of customers belong to this category. Companies can also target these customers given the fact that they are
# in huge numbers, etc.
# =============================================================================
