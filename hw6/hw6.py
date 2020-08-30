"""
Joanne Kwon
Professor Cai
PIC 16
February 26, 2019
"""

'''
PROBLEM 1
Function heart(im) takes in an image and outputs a heart-shaped cut-out of it on a pink background.
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

def heart(im):
    img=mpimg.imread(im)
    plt.figure(figsize=(7,7)) #image size
    dd=np.zeros_like(img) #array of zeros with the same shape/type
    h,w,_=dd.shape #height/width

    #base triangle
    cv2.fillPoly(dd,[np.array([[w-w,h/2],[w,h/2],[w/2,h]])],(255,255,255))
    #rectangle
    cv2.fillPoly(dd,[np.array([[w-w,h/2],[w,h/2],[w,(h/6)*2],[w-w,(h/6)*2]])],(255,255,255))
    #ellipses
    cv2.ellipse(dd,((w/4)*3,(h/6)*2),(w/4,(h/6)*2),180,0,180,(255,255,255),-1) #right
    cv2.ellipse(dd,((w/4),(h/6)*2),(w/4,(h/6)*2),180,0,180,(255,255,255),-1) #left
    
    final=cv2.bitwise_and(dd,img) #combined
    final[np.where((final==[0,0,0]).all(axis=2))]=[255,192,203] #pink background
    #heart-shape output
    plt.title('Heart-Shaped Image')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(final)
    plt.show()
    
    ##########
    #ALTERNATIVE METHOD
    img=mpimg.imread(im)
    imgc=img.copy() #copy of image
    plt.figure(figsize=(7,7)) #image size
    h,w,_=imgc.shape #height/width
    y,x=np.ogrid[0:h,0:w] #x & y meshgrid values
    img=img[:,:,:3]
    
    #pink background
    pink=np.zeros_like(imgc)
    if np.max(img)<=1:
        pink[:,:,:]=(255./255,192./255,203./255)
    else:
        pink[:,:,:]=(255,192,203)
    
    mask1=(y+x<h+(w/2)) #bottom right
    mask2=(y-x<h-(w/2)) #bottom left
    mask3=((x-w/4)**2+(y-h/4)**2<(w/4)**2)|(y>h/4) #top left
    mask4=((x-3*w/4)**2+(y-h/4)**2<(w/4)**2)|(y>h/4) #top right
    pink[mask1&mask2&(mask3|mask4)]=imgc[mask1&mask2&(mask3|mask4)] #combined
    #heart-shape output (alternative)
    plt.title('Heart-Shaped Image (Alternative)')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(pink)
    plt.show()
    
#test case
heart('kitty-cat.jpg')


'''
PROBLEM 2
Function blurring(im,method) takes in an image and outputs a gray-scale image with options for either
uniform or Gaussian noise removal (blurring). Users can input either 'uniform' or 'gaussian' to use 
their respective functionalities.
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2

def blurring(im,method):
    img=cv2.imread(im,0)
    plt.figure(figsize=(15,15)) #image size

    if method=='gaussian': #gaussian noise removal
        plt.subplot(2,2,1)
        g_blur=cv2.GaussianBlur(img,(5,5),0) #blurs image using gaussian filter
        plt.imshow(g_blur,cmap='gray') #apply gaussian blur filter & gray-scale
        plt.title('Gaussian')
        plt.xticks([])
        plt.yticks([])
    elif method=='uniform': #uniform noise removal
        plt.subplot(2,2,2)
        u_blur=cv2.blur(img,(5,5)) #blurs image using normalized box filter
        plt.imshow(u_blur,cmap='gray') #apply uniform blur filter & gray-scale
        plt.title('Uniform')
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
#test cases
blurring('kitty-cat.jpg','gaussian')
blurring('kitty-cat.jpg','uniform')


'''
PROBLEM 3
Function detect_edge(im,method) takes in an image and outputs a gray-scale image with options to detect 
horizontal, vertical, or both horizontal and vertical edges within the image. Users can input either 
'horizontal,' 'vertical,' or 'both' to use their respective functionalities.
'''
import matplotlib.pyplot as plt
import numpy as np
import cv2

def detect_edge(im,method):
    img=cv2.imread(im,0)
    plt.figure(figsize=(15,15)) #image size
    
    if method=='horizontal': #horizontal edge detection
        plt.subplot(2,2,1)
        y_sobel=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3) #sobel y filter
        plt.imshow(y_sobel,cmap='gray') #apply y sobel & gray-scale
        plt.title('Horizontal')
        plt.xticks([])
        plt.yticks([])
    elif method=='vertical': #vertical edge detection
        plt.subplot(2,2,2)
        x_sobel=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3) #sobel x filter
        plt.imshow(x_sobel,cmap='gray') #apply x sobel & gray-scale
        plt.title('Vertical')
        plt.xticks([])
        plt.yticks([])
    elif method=='both': #edge detection for both
        plt.subplot(2,2,3)
        #edges = cv2.Canny(img,200,100)
        laplacian=cv2.Laplacian(img,cv2.CV_64F) #laplacian filter
        plt.imshow(laplacian,cmap='gray') #apply laplacian & gray-scale
        plt.title('Both')
        plt.xticks([])
        plt.yticks([])
    plt.show()

#test cases
detect_edge('kitty-cat.jpg','horizontal')
detect_edge('kitty-cat.jpg','vertical')
detect_edge('kitty-cat.jpg','both')



