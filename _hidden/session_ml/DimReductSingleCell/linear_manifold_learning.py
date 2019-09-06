#!/usr/bin/python

# This script processes takes a matrix with features as columns and samples as rows (last column is cluster assignment i.e. 1, 2, 3 etc.) and generates a number of
# a) linear dimensionality reduction plots (PCA, MDS, Factor Analysis, ICA), b) non-linear dimensionality reduction plots (tSNE, LLE, Isomaps, Laplacian Eigenmaps etc.)
# Nikolay Oskolkov, WABI Long-Term Support, nikolay.oskolkov@scilifelab.se
# Usage: python manifold_learning.py /home/nikolay/WABI/K_Pietras/Manifold_Learning/filtered_expr_rpkm.txt

import sys
import math
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.decomposition import FastICA
from sklearn.decomposition import SparsePCA
from sklearn.decomposition import TruncatedSVD
from sklearn.manifold import SpectralEmbedding
from sklearn.decomposition import FactorAnalysis
from sklearn.ensemble import RandomTreesEmbedding
from sklearn.manifold import LocallyLinearEmbedding
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

import warnings
warnings.filterwarnings("ignore")

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
################################################################################################# LINEAR DIMENSIONALITY REDUCTION ##################################################################################################
####################################################################################################################################################################################################################################

# PREPARE TO PLOT LINEAR DIMENSIONALITY REDUCTION
print("Start Making Linear Dimensionality Reduction Plots ... \n")
fig = plt.figure(1)
mpl.rcParams.update({'font.size': 5})

# PRINCIPAL COMPONENT ANALYSIS (PCA)
print("Performing Principal Component Analysis (PCA) ...")
plt.subplot(331)
X_reduced = PCA(n_components = 2).fit_transform(X)
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Principal Component Analysis (PCA)')
#plt.colorbar()
plt.xlabel("PCA1")
plt.ylabel("PCA2")

# INDEPENDENT COMPONENT ANALYSIS (ICA)
print("Performing Independent Component Analysis (ICA) ...")
plt.subplot(332)
model = FastICA(n_components = 2)
ica = model.fit_transform(X)
plt.scatter(ica[:, 0], ica[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Independent Component Analysis (ICA)')
#plt.colorbar()
plt.xlabel("ICA1")
plt.ylabel("ICA2")

# FACTOR ANALYSIS (FA)
print("Performing Factor Analysis (FA) ...")
plt.subplot(333)
model = FactorAnalysis(n_components = 2)
fa = model.fit_transform(X)
plt.scatter(fa[:, 0], fa[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Factor Analysis (FA)')
#plt.colorbar()
plt.xlabel("FA1")
plt.ylabel("FA2")

# NONNEGATIVE MATRIX FACTORIZATION (NMF)
print("Performing Non-negative Matrix Factorization (NMF) ...")
plt.subplot(334)
model = NMF(n_components = 2, solver = 'cd', beta_loss = 'frobenius')
nmf = model.fit_transform(X)
plt.scatter(nmf[:, 0], nmf[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Non-negative Matrix Factorization (NMF)')
#plt.colorbar()
plt.xlabel("NMF1")
plt.ylabel("NMF2")

# METRIC MULTI-DIMENSIONAL SCALING (MMDS)
print("Performing Metric Multi-Dimensional Scaling (MMDS) ...")
plt.subplot(335)
model_mds = MDS(n_components = 2, random_state = 1, metric = True, n_jobs = -1)
mmds = model_mds.fit_transform(X)
plt.scatter(mmds[:, 0], mmds[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Metric Multi-Dimensional Scaling (MMDS)')
#plt.colorbar()
plt.xlabel("MMDS1")
plt.ylabel("MMDS2")

# NONMETRIC MULTI-DIMENSIONAL SCALING (NMDS)
print("Performing Non-Metric Multi-Dimensional Scaling (NMDS) ...")
plt.subplot(336)
model_nnmds = MDS(n_components = 2, random_state = 1, metric = False, n_jobs = -1, max_iter = 3000, eps = 1e-12, n_init = 1)
init_mmds = model_mds.fit(X).embedding_
nmds = model_nnmds.fit_transform(X, init = init_mmds) # use metric mds as a starting configuration
plt.scatter(nmds[:, 0], nmds[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Non-Metric Multi-Dimensional Scaling (NMDS)')
#plt.colorbar()
plt.xlabel("NMDS1")
plt.ylabel("NMDS2")
              
# SINGULAR VALUE DECOMPOSITION (SVD)
print("Performing Singular Value Decomposition (SVD) ...")
plt.subplot(337)
model = TruncatedSVD(n_components = 2)
svd = model.fit_transform(X)
plt.scatter(svd[:, 0], svd[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Singular Value Decomposition (SVD)')
##plt.colorbar()
plt.xlabel("SVD1")
plt.ylabel("SVD2")

# SPARSE PRINCIPAL COMPONENT ANALYSIS (SPCA)
print("Performing Sparse Principal Component Analysis (SPCA) ...")
plt.subplot(338)
spca = SparsePCA(n_components = 2, n_jobs = -1).fit_transform(X)
plt.scatter(spca[:, 0], spca[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Sparse Principal Component Analysis (SPCA)')
#plt.colorbar()
plt.xlabel("SPC1")
plt.ylabel("SPC2")

# LINEAR DISCRIMINANT ANALYSIS (LDA)
print("Performing Linear Discriminant Analysis (LDA) ...")
plt.subplot(339)
model = LinearDiscriminantAnalysis(n_components = 2, priors = None, shrinkage = 'auto', solver = 'eigen', store_covariance = False, tol = 0.0001)
lda = model.fit_transform(X, Y)
#print(model.coef_)
plt.scatter(lda[:, 0], lda[:, 1], c = Y, cmap = 'viridis', s = 1)
plt.title('Linear Discriminant Analysis (LDA)')
#plt.colorbar()
plt.xlabel("LDA1")
plt.ylabel("LDA2")
print("\n Feature Importances: \n")
feature_importances = pd.DataFrame({'Gene':np.array(expr.columns)[:-1], 'Score':abs(model.coef_[0])})
print(feature_importances.sort_values('Score', ascending = False).head(20))

# LOCAL TANGENT SPACE ALIGNMENT (LTSA)
#print("Performing Local Tangent Space Alignment (LTSA) ...")
#plt.subplot(338)
#model = LocallyLinearEmbedding(n_components = 2, method = 'ltsa', n_neighbors = 30, eigen_solver = 'dense')
#ltsa = model.fit_transform(X)
#plt.scatter(ltsa[:, 0], ltsa[:, 1], c = Y, cmap = 'viridis', s = 1)
#plt.title('Local Tangent Space Alignment (LTSA)')
##plt.colorbar()
#plt.xlabel("LTSA1")
#plt.ylabel("LTSA2")

# LATENT DIRICHLET ALLOCATION (LDirA)
#print("Performing Latent Dirichlet Allocation (LDirA) ...")
#plt.subplot(339)
#model = LatentDirichletAllocation(n_components = 2, learning_method = 'batch')
#ldira = model.fit_transform(X)
#plt.scatter(ldira[:, 0], ldira[:, 1], c = Y, cmap = 'viridis', s = 1)
#plt.title('Latent Dirichlet Allocation (LDirA)')
##plt.colorbar()
#plt.xlabel("LDirA1")
#plt.ylabel("LDirA2")

# SAVE LINEAR DIMENSIONALITY REDUCTION PLOTS AS PDF
print("\n")
plt.tight_layout()
#plt.show()
fig.savefig('linear_manifold_learning.pdf')
