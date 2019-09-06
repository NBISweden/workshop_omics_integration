#!/usr/bin/python

# This script processes takes a matrix with features as columns and samples as rows (last column is cluster assignment i.e. 1, 2, 3 etc.) and generates a number of
# a) linear dimensionality reduction plots (PCA, MDS, Factor Analysis, ICA), b) non-linear dimensionality reduction plots (tSNE, LLE, Isomaps, Laplacian Eigenmaps etc.)
# Nikolay Oskolkov, WABI Long-Term Support, nikolay.oskolkov@scilifelab.se
# Usage: python manifold_learning.py /home/nikolay/WABI/K_Pietras/Manifold_Learning/filtered_expr_rpkm.txt

import sys
import math
import numpy as np
import pandas as pd
from umap import UMAP
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.decomposition import FastICA
from sklearn.decomposition import KernelPCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import SpectralEmbedding
from sklearn.decomposition import FactorAnalysis
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# READ DATA
infile = str(sys.argv[1])
print("\n" + "You specified input file: " + infile + "\n")

expr = pd.read_csv(infile,sep='\t')
print("\n" + "Dimensions of input file: " + str(expr.shape) + "\n")
print("\n" + "A few first lines of input file: " + "\n")
print(expr.iloc[0:4, 0:4])
print("\n" + "Last column corresponds to cluster assignments: " + "\n")
print(expr.iloc[0:4, (expr.shape[1]-4):expr.shape[1]])

# LOG-TRANSFORM DATA
X = expr.values[:,0:(expr.shape[1]-1)]
Y = expr.values[:,expr.shape[1]-1]
print("\n" + "A few cluster labels: " + "\n")
print(Y[0:8])
print("\n" + "Number of unique clusters: " + str(len(set(Y))) + "\n")
print("\n" + "You have following unique cluster labels: " + "\n")
print(set(Y))
print("\n" + "Log-transforming data..." + "\n")
X = np.log(X + 1)

####################################################################################################################################################################################################################################
################################################################################################# NON-LINEAR DIMENSIONALITY REDUCTION ##############################################################################################
####################################################################################################################################################################################################################################

# PREPARE TO PLOT NON-LINEAR DIMENSIONALITY REDUCTION
print("Start Making Non-Linear Dimensionality Reduction Plots ... \n")
fig = plt.figure(1)
mpl.rcParams.update({'font.size': 5})

# LOCALLY LINEAR EMBEDDING (LLE)
print("Performing Locally Linear Embedding (LLE) ...")
plt.subplot(331)
model = LocallyLinearEmbedding(n_components = 2, n_neighbors = 50, method = 'standard')
lle = model.fit_transform(X)
plt.scatter(lle[:, 0], lle[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Locally Linear Embedding (LLE)')
#plt.colorbar()
plt.xlabel("LLE1")
plt.ylabel("LLE2")

# MODIFIED LOCALLY LINEAR EMBEDDING (LLE)
print("Performing Modified Locally Linear Embedding (MLLE) ...")
plt.subplot(332)
model = LocallyLinearEmbedding(n_neighbors = 20, n_components = 2, method = 'modified', eigen_solver = 'dense')
mlle = model.fit_transform(X)
plt.scatter(mlle[:, 0], mlle[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Modified Locally Linear Embedding (LLE)')
#plt.colorbar()
plt.xlabel("MLLE1")
plt.ylabel("MLLE2")

# KERNEL PRINCIPAL COMPONENT ANALYSIS (KPCA)
print("Performing Kernel Principal Component Analysis (KPCA) ...")
plt.subplot(333)
kpca = KernelPCA(n_components = 2, kernel = 'cosine').fit_transform(X)
plt.scatter(kpca[:, 0], kpca[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Kernel PCA')
#plt.colorbar()
plt.xlabel("KPCA1")
plt.ylabel("KPCA2")

# ISOMAP
print("Performing Isomap Plotting ...")
plt.subplot(334)
model = Isomap(n_components = 2)
isomap = model.fit_transform(X)
plt.scatter(isomap[:, 0], isomap[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Isomap')
#plt.colorbar()
plt.xlabel("ISO1")
plt.ylabel("ISO2")

# LAPLACIAN EIGENMAP
print("Performing Laplacian Eigenmap (Spectral Embedding) ...")
plt.subplot(335)
model = SpectralEmbedding(n_components = 2, n_neighbors = 50)
se = model.fit_transform(X)
plt.scatter(se[:, 0], se[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Laplacian Eigenmap')
#plt.colorbar()
plt.xlabel("LAP1")
plt.ylabel("LAP2")

# RANDOM FOREST EMBEDDING
print("Performing Random Forest Embedding (RFE) ...")
plt.subplot(336)
hasher = RandomTreesEmbedding(n_estimators = 200, random_state = 1, max_depth = 5)
X_transformed = hasher.fit_transform(X)
model = TruncatedSVD(n_components = 2)
svd = model.fit_transform(X_transformed)
plt.scatter(svd[:, 0], svd[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Random Forest Embedding (RFE)')
#plt.colorbar()
plt.xlabel("RFE1")
plt.ylabel("RFE2")

# T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING (tSNE)
print("Performing T-Distributed Stochastic Neighbor Embedding (tSNE) ...")
plt.subplot(337)
model = TSNE(learning_rate = 10, n_components = 2, random_state = 123, perplexity = 30)
tsne = model.fit_transform(X)
plt.scatter(tsne[:, 0], tsne[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('tSNE')
#plt.colorbar()
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")

# T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING (tSNE) ON PCA
print("Performing T-Distributed Stochastic Neighbor Embedding (tSNE) on PCA ...")
plt.subplot(338)
X_reduced = PCA(n_components = 30).fit_transform(X)
model = TSNE(learning_rate = 10, n_components = 2, random_state = 123, perplexity = 30)
tsne = model.fit_transform(X_reduced)
plt.scatter(tsne[:, 0], tsne[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('tSNE on PCA')
#plt.colorbar()
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")

# UNIFORM MANIFOLD APPROXIMATION AND PROJECTION (UMAP)
print("Performing Uniform Manifold Approximation and Projection (UMAP) ...")
plt.subplot(339)
model = UMAP(n_neighbors = 30, min_dist = 0.3, n_components = 2)
umap = model.fit_transform(X_reduced)
plt.scatter(umap[:, 0], umap[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('UMAP')
#plt.colorbar()
plt.xlabel("UMAP1")
plt.ylabel("UMAP2")

# HESSIAN LOCALLY LINEAR EMBEDDING (HLLE)
#print("Performing Hessian Locally Linear Embedding (HLLE) ...")
#plt.subplot(333)
#model = LocallyLinearEmbedding(n_components = 2, method = 'hessian', n_neighbors = 20, eigen_solver = 'dense', hessian_tol=0.0001)
#hlle = model.fit_transform(X)
#print(hlle[:, 0])
#plt.scatter(hlle[:, 0], hlle[:, 1], c = Y, cmap = 'viridis', s = 1)
#plt.title('Hessian Locally Linear Embedding (HLLE)')
##plt.colorbar()
#plt.xlabel("HLLE1")
#plt.ylabel("HLLE2")

# SAVE NON-LINEAR DIMENSIONALITY REDUCTION PLOTS AS PDF
print("\n")
plt.tight_layout()
#plt.show()
fig.savefig('non_linear_manifold_learning.pdf')

