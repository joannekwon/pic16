"""
Joanne Kwon
PIC 16
Professor Cai
March 8, 2019
"""

'''
HOMEWORK 7
Train a Support Vector Classifier to read my handwriting. Not completed.
'''
from scipy.misc import imread # using scipy's imread
import matplotlib.pyplot as plt
import numpy as np
from skimage.transform import resize
from sklearn import svm

#boundaries and separate function separates image into separate files for each letter
def boundaries(binarized,axis):
    # variables named assuming axis = 0; algorithm valid for axis=1
    # [1,0][axis] effectively swaps axes for summing
    rows = np.sum(binarized,axis = [1,0][axis]) > 0
    rows[1:] = np.logical_xor(rows[1:], rows[:-1])
    change = np.nonzero(rows)[0]
    ymin = change[::2]
    ymax = change[1::2]
    height = ymax-ymin
    too_small = 10 # real letters will be bigger than 10px by 10px
    ymin = ymin[height>too_small]
    ymax = ymax[height>too_small]
    return zip(ymin,ymax)

def separate(img):
    orig_img = img.copy()
    pure_white = 255.
    white = np.max(img)
    black = np.min(img)
    thresh = (white+black)/2.0
    binarized = img<thresh
    row_bounds = boundaries(binarized, axis = 0) 
    cropped = []
    for r1,r2 in row_bounds:
        img = binarized[r1:r2,:]
        col_bounds = boundaries(img,axis=1)
        rects = [r1,r2,col_bounds[0][0],col_bounds[0][1]]
        cropped.append(np.array(orig_img[rects[0]:rects[1],rects[2]:rects[3]]/pure_white))
    return cropped

#partition function accepts data arrays, target arrays, and percentage of data used for training (part 5)
def partition(data,target,p):
    train_data=data*p
    test_data=data-train_data
    train_target=target*p
    test_target=target-train_data
    return train_data,train_target,test_data,test_target

big_img = imread("a.jpg", flatten = True) # flatten = True converts to grayscale
plt.imshow(big_img/255,cmap='gray')

#separates big_img (pure white = 255) into array of little images (pure white = 1.0)
imgs = separate(big_img) 
for img in imgs:
    img = resize(img, (10,10))
    plt.imshow(img, cmap='gray')

#0 used to represent a, 1 used to represent b, 2 used to represent c (part 3)
labels=[]
for i in range(3):
    for j in range(23):
        labels.append(i)
        
#convert image array to data array to contain 23 a's, 23 b's, 23 c's
        
partition(data_array,labels,p=0.5)
        
#SVC (part 6)
classifier=svm.SVC(gamma=0.001, C=100)
classifier.fit(dataset,labels)

predicted=classifier.predict(a_test) #predicted will give you either 0, 1, or 2

print "Predicted:", predicted
print "Truth:", truth
print "Accuracy:", accuracy
