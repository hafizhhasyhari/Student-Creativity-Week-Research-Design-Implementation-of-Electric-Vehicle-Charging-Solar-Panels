import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Simulasi data konsumsi energi
np.random.seed(42)
data = np.random.rand(20, 2) * [100, 50] + [50, 30]  # Konsumsi energi dan variabilitasnya
df = pd.DataFrame(data, columns=['Energy_Consumption', 'Variation'])

# Normalisasi data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df)

# Agglomerative Clustering
linkage_matrix = linkage(data_scaled, method='ward')

# Plot Dendrogram
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix, labels=np.arange(1, len(data) + 1))
plt.title('Dendrogram - Agglomerative Hierarchical Clustering')
plt.xlabel('Data Points')
plt.ylabel('Euclidean Distance')
plt.show()

# Tentukan jumlah cluster (misal 3)
clusters = fcluster(linkage_matrix, t=3, criterion='maxclust')
df['Cluster'] = clusters

print(df.sort_values('Cluster'))
