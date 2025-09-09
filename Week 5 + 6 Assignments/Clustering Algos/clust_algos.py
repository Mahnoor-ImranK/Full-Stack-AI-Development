import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import adjusted_rand_score, silhouette_score
from sklearn.datasets import load_iris

#Load dataset
iris = load_iris()
X, y_true = iris.data, iris.target

#clustering models
clustering_models = {
    "KMeans": KMeans(n_clusters=3, random_state=42),
    "Agglomerative": AgglomerativeClustering(n_clusters=3),
    "DBSCAN": DBSCAN(eps=0.6, min_samples=5)
}

#train & evaluate
cluster_results = []
for name, model in clustering_models.items():
    labels = model.fit_predict(X)
    
    ari = adjusted_rand_score(y_true, labels)
    sil = silhouette_score(X, labels) if len(set(labels)) > 1 else -1
    
    print(f"\n{name} Results:")
    print("Adjusted Rand Index:", ari)
    print("Silhouette Score:", sil)
    print("Cluster Labels Distribution:", np.bincount(labels + abs(min(labels))))
    
    cluster_results.append([name, ari, sil])

# 4. Show summary
df_cluster_results = pd.DataFrame(cluster_results, columns=["Model", "ARI", "Silhouette"])
print("\n=== Clustering Summary ===")
print(df_cluster_results)
