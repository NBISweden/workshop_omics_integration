#!/usr/bin/python
# Nikolay Oskolkov, WABI Long-Term Support, nikolay.oskolkov@scilifelab.se

import sys
import keras
import numpy as np
import pandas as pd
from keras import regularizers
from keras.layers import Dense
import matplotlib.pyplot as plt
from keras.layers import Dropout
from sklearn.manifold import TSNE
from keras.optimizers import Adam
from sklearn.decomposition import PCA
from keras.models import Sequential, Model

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
print("\n" + "You have following unique cluster labels: " + "\n")
print(set(Y))
print("\n" + "Log-transforming data..." + "\n")
X = np.log(X + 1)

# REDUCE DIMENSIONS WITH PRINCIPAL COMPONENT ANALYSIS (PCA)
n_input = 10
x_train = PCA(n_components = n_input).fit_transform(X)
y_train = Y
#plt.figure(figsize=(20, 15))
plt.scatter(x_train[:, 0], x_train[:, 1], c = y_train, cmap = 'tab20', s = 10)
plt.title('Principal Component Analysis (PCA)')
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
print("\n" + "Dimensions of reduced data set: " + str(x_train.shape) + "\n")

# REDUCE DIMENSIONS WITH T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING (tSNE)
model_tsne = TSNE(learning_rate = 200, n_components = 2, random_state = 123, perplexity = 90, n_iter = 1000, verbose = 1)
tsne = model_tsne.fit_transform(x_train)
#plt.figure(figsize=(20, 15))
plt.scatter(tsne[:, 0], tsne[:, 1], c = y_train, cmap = 'tab20', s = 10)
plt.title('tSNE on PCA')
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")
plt.show()

# REDUCE DIMENSIONS WITH AUTOENCODER
model = Sequential()
model.add(Dropout(0.2,  input_shape=(X.shape[1],)))
model.add(Dense(10,     activation = 'elu'))
model.add(Dense(8,      activation = 'elu'))
model.add(Dense(6,      activation = 'elu'))
model.add(Dense(4,      activation = 'linear', name = "bottleneck"))
model.add(Dense(6,      activation = 'elu'))
model.add(Dense(8,      activation = 'elu'))
model.add(Dense(10,     activation = 'elu'))
model.add(Dense(X.shape[1],   activation = 'sigmoid'))
model.compile(loss = 'mean_squared_error', optimizer = Adam())
model.summary()

history = model.fit(X, X, batch_size = 128, epochs = 100, shuffle = True, verbose = 1, validation_split = 0.2)
print("\n" + "Training Accuracy: ", history.history['loss'][-1])
print("Validation Accuracy: ", history.history['val_loss'][-1], "\n")
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validate'], loc='upper right')
plt.show()

encoder = Model(model.input, model.get_layer('bottleneck').output)
bottleneck_representation = encoder.predict(X)

model_tsne_auto = TSNE(learning_rate = 200, n_components = 2, random_state = 123, perplexity = 90, n_iter = 1000, verbose = 1)
tsne_auto = model_tsne_auto.fit_transform(bottleneck_representation)
#plt.figure(figsize=(20, 15))
plt.scatter(tsne_auto[:, 0], tsne_auto[:, 1], c = Y, cmap = 'tab20', s = 10)
plt.title('tSNE on Autoencoder: 8 Layers')
plt.xlabel("tSNE1")
plt.ylabel("tSNE2")
plt.show()

# VISUALIZE AUTOENCODER
#from ann_visualizer.visualize import ann_viz
#ann_viz(model, title = "Autoencoder", view = True)
