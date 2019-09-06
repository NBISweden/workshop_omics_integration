#!/usr/bin/python
# Nikolay Oskolkov, WABI Long-Term Support, nikolay.oskolkov@scilifelab.se

import os
import numpy as np
import pandas as pd
from umap import UMAP
import matplotlib as mpl
from sklearn.manifold import TSNE
from keras.layers import Input, Dense, Dropout
from keras.layers.merge import concatenate
from keras.models import Model
from keras.utils import plot_model
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

########################################## READ AND TRANSFORM DATA ##############################################
os.chdir("/home/nikolay/WABI/Misc/SingleCell/CITEseq/")
scRNAseq = pd.read_csv('scRNAseq.txt',sep='\t')
scProteomics = pd.read_csv('scProteomics.txt',sep='\t')
print(scRNAseq.shape)
print(scProteomics.shape)
print("\n")
print(scRNAseq.iloc[0:5,0:5])
print(scProteomics.iloc[0:5,0:5])

X_scRNAseq = scRNAseq.values[:,0:(scRNAseq.shape[1]-1)]
Y_scRNAseq = scRNAseq.values[:,scRNAseq.shape[1]-1]
X_scProteomics = scProteomics.values[:,0:(scProteomics.shape[1]-1)]
Y_scProteomics = scProteomics.values[:,scProteomics.shape[1]-1]
print("\n")
print(X_scRNAseq[0:5,0:5])
print(Y_scRNAseq[0:5])

# LOG-TRANSFORM DATA
X_scRNAseq = np.log(X_scRNAseq + 1)
print(X_scRNAseq[0:5,0:5])
X_scProteomics = np.log(X_scProteomics + 1)
print(X_scProteomics[0:5,0:5])

################################################## AUTOENCODER ##################################################

# Input Layer
ncol_scRNAseq = X_scRNAseq.shape[1]
input_dim_scRNAseq = Input(shape = (ncol_scRNAseq, ), name = "scRNAseq")
ncol_scProteomics = X_scProteomics.shape[1]
input_dim_scProteomics = Input(shape = (ncol_scProteomics, ), name = "scProteomics")

# Dimensions of Encoder for each OMIC
encoding_dim_scRNAseq = 50
encoding_dim_scProteomics = 10

# Encoder layer for each OMIC
encoded_scRNAseq = Dense(encoding_dim_scRNAseq, activation = 'linear', name = "Encoder_scRNAseq")(input_dim_scRNAseq)
encoded_scProteomics = Dense(encoding_dim_scProteomics, activation = 'linear', name = "Encoder_scProteomics")(input_dim_scProteomics)

# Merging Encoder layers from different OMICs
merge = concatenate([encoded_scRNAseq, encoded_scProteomics])

# Bottleneck compression
bottleneck = Dense(50, kernel_initializer = 'uniform', activation = 'linear', name = "Bottleneck")(merge)

#Inverse merging
merge_inverse = Dense(encoding_dim_scRNAseq + encoding_dim_scProteomics, activation = 'elu', name = "Concatenate_Inverse")(bottleneck)

# Decoder layer for each OMIC
decoded_scRNAseq = Dense(ncol_scRNAseq, activation = 'sigmoid', name = "Decoder_scRNAseq")(merge_inverse)
decoded_scProteomics = Dense(ncol_scProteomics, activation = 'sigmoid', name = "Decoder_scProteomics")(merge_inverse)

# Combining Encoder and Decoder into an Autoencoder model
autoencoder = Model(input = [input_dim_scRNAseq, input_dim_scProteomics], output = [decoded_scRNAseq, decoded_scProteomics])

# Compile Autoencoder
autoencoder.compile(optimizer = 'adam', loss={'Decoder_scRNAseq': 'mean_squared_error', 'Decoder_scProteomics': 'mean_squared_error'})
autoencoder.summary()

# Autoencoder graph
plot_model(autoencoder, to_file='autoencoder_graph.png')

# Autoencoder training
estimator = autoencoder.fit([X_scRNAseq, X_scProteomics], [X_scRNAseq, X_scProteomics], epochs = 100, batch_size = 128, validation_split = 0.2, shuffle = True, verbose = 1)
print("Training Loss: ",estimator.history['loss'][-1])
print("Validation Loss: ",estimator.history['val_loss'][-1])
#plt.figure(figsize=(20, 15))
plt.plot(estimator.history['loss'])
plt.plot(estimator.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train','Validation'], loc = 'upper right')
plt.show()

# Encoder model
encoder = Model(input = [input_dim_scRNAseq, input_dim_scProteomics], output = bottleneck)
bottleneck_representation = encoder.predict([X_scRNAseq, X_scProteomics])
print(pd.DataFrame(bottleneck_representation).shape)
print(pd.DataFrame(bottleneck_representation).iloc[0:5,0:5])

# Dimensionality reduction plot
#plt.figure(figsize=(20, 15))
plt.scatter(bottleneck_representation[:, 0], bottleneck_representation[:, 1], c = Y_scRNAseq, cmap = 'tab20', s = 10)
plt.title('Autoencoder Data Integration')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
#plt.colorbar()
plt.show()

# tSNE on Autoencoder bottleneck representation
model_tsne_auto = TSNE(learning_rate = 200, n_components = 2, random_state = 123, perplexity = 90, n_iter = 1000, verbose = 1)
tsne_auto = model_tsne_auto.fit_transform(bottleneck_representation)
plt.scatter(tsne_auto[:, 0], tsne_auto[:, 1], c = Y_scRNAseq, cmap = 'tab20', s = 10)
plt.title('tSNE on Autoencoder: Data Integration, CITEseq')
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")
plt.show()

# UNIFORM MANIFOLD APPROXIMATION AND PROJECTION (UMAP)
#model_umap = UMAP(n_neighbors = 20, min_dist = 0.3, n_components = 2)
#umap = model_umap.fit_transform(bottleneck_representation)
#plt.scatter(umap[:, 0], umap[:, 1], c = Y_scRNAseq, cmap = 'tab20', s = 10)
#plt.title('UMAP on Autoencoder')
#plt.xlabel("UMAP1")
#plt.ylabel("UMAP2")
#plt.show()
