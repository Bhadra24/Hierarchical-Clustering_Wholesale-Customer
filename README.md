# Hierarchical-Clustering_Wholesale-Customer
Clustering:
Clustering is the method of dividing objects into sets that are similar, and dissimilar to the objects belonging to another set. There are two different types of clustering, each divisible into two subsets
•Hierarchical clustering: 1) Agglomerative 2) Divisive 
•Partial clustering: 1) K-means 2) Fuzzy c-means

Hierarchical Clustering: 
Hierarchical clustering is a method of cluster analysis, which seeks to build a hierarchy of clusters. Hierarchical clustering came before K-Means clustering. A diagram called a dendrogram (A tree diagram that statistics the sequence of merge or splits)

What are the different methods of hierarchical clustering?

•Agglomerative – Also called bottom-up approach. Each observation starts in its own cluster and pairs of clusters are merged as one moves up the hierarchy.

•Divisive – Also called the top-down approach. All observations start in one cluster, and splits are performed recursively as one moves down the hierarchy

Steps to Perform Hierarchical Clustering:

1)Compute the proximity matrix

2)Let each data point be a cluster
3)Repeat Step2: Combine the 2 closest clusters ( by calculating the distance between these clusters) and accordingly update the proximity matrix.
4)Until only a Singular cluster remains.
