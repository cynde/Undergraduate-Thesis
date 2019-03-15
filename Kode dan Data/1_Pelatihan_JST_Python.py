# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 09:32:01 2018

@author: cynde_
"""
from sklearn.neural_network import MLPClassifier
import os
import cv2
from os import listdir
import numpy as np
import time

start = time.time()

#output
class_0 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
class_1 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
class_2 = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
class_3 = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
class_4 = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
class_5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
class_6 = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
class_7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
class_8 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
class_9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
array_class = [class_0, class_1, class_2, class_3, class_4, class_5, class_6, class_7, class_8, class_9]

#process the images
print("Processing the images..")
images = np.empty((0,600), float)
labels = np.empty((0,10), float)
os.chdir("dataset_scaled_only")
a = 0

path = os.getcwd()
for file in listdir(path):
    a += 1
    print("Image " + str(a))
    img = cv2.imread(file)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_th = cv2.threshold(img_gray, 0, 1, cv2.THRESH_BINARY_INV) 
    if(img_th.shape[0] != 30 or img_th.shape[1] != 20):
        img_th = cv2.resize(img_th, (20, 30), interpolation = cv2.INTER_CUBIC)
    images = np.append(images, np.array([img_th.ravel().tolist()], float), axis=0)
    labels = np.append(labels, np.array([array_class[int(os.path.splitext(file)[0].split('_')[0])]], float), axis=0)
os.chdir("../")

start_training = time.time()

#train
print("Training..")                         
mlp = MLPClassifier(hidden_layer_sizes=(40), max_iter=1, alpha=1e-4, activation='logistic',
                    solver='adam', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.01, warm_start=True)

epoch = 12000
for i in range(epoch):
    mlp.fit(images, labels)

print("Training set score: %f" % mlp.score(images, labels))

end = time.time()

print("Time to training & testing: " + str(end - start_training))
#print("Time for all: " + str(end - start))

#save the weights & biases to csv
weights = mlp.coefs_
biases = mlp.intercepts_

rounded_weights = []
for j in weights:
    j = np.round(j,2)
    rounded_weights.append(j)
    
rounded_biases = []
for j in biases:
    j = np.round(j,2)
    rounded_biases.append(j)
    
np.savetxt("rounded_weights_1.csv", rounded_weights[0], fmt='%.2f', delimiter=",")
np.savetxt("rounded_weights_2.csv", rounded_weights[1], fmt='%.2f', delimiter=",")
np.savetxt("rounded_biases_1.csv", rounded_biases[0], fmt='%.2f', delimiter=",")
np.savetxt("rounded_biases_2.csv", rounded_biases[1], fmt='%.2f', delimiter=",")

