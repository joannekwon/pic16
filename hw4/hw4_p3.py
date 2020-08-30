"""
Joanne Kwon
PIC 16
Professor Cai
February 11, 2019
"""

'''
HOMEWORK 4 PROBLEM 3
Utilize labels, directed edges, colors, different types of nodes/edges, nodes belonging to
different groups, etc. to visualize a small network with a good amount of information.
Created two different networks. (1) Five Star Constellation Network which used encoded data
and (2) Network of European Emails which used the dataset from https://snap.stanford.edu/data/email-Eu-core.html.
'''

import matplotlib.pyplot as plt
import numpy as np

#NETWORK 1: network of five star constellation
stars=[[0,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[0,1,1,0,1]] #directed edges & nodes belonging to different groups

n=len(stars)
for i in range(n): #equally plot nodes in a circle
    x=[np.cos(2*np.pi*i/n) for i in range(n)]
    y=[np.sin(2*np.pi*i/n) for i in range(n)]
plt.plot(x,y,'m*') #use of different colors/design for nodes

for i in range(n): #create connections between nodes 
    for j in range(n):
        if stars[i][j]==1:
            plt.plot([x[i],x[j]],[y[i],y[j]],'c--') #use of differnt color/design for edges
   
plt.xlabel('Horizontal (x-axis)') #label for x-axis
plt.ylabel('Vertical (y-axis)') #label for y-axis
plt.title('Five Star Constellation Network') #title
plt.show()


#NETWORK 2: network of emails
emails=open("email.csv").read()
#prep data for easier utilization; split by pair/list
pairs=[s.split('\t') for s in emails.splitlines()]
pairs=[[int(i) for i in j]for j in pairs]
#prep for matrix; value to 0 then made 1 if applicable
m=max(max(j for j in pairs))
matrix=[[0]*m for k in range(m)]
for p in pairs:
    matrix[p[0]-1][p[1]-1]=1
    matrix[p[1]-1][p[0]-1]=1

#process of plotting nodes and creating connections in network
x=[]
y=[]
n=len(matrix)

for i in range(n): #equally plots nodes in a circle
    x.append(np.cos(2*np.pi/n*i)*100)
    y.append(np.sin(2*np.pi/n*i)*100)
plt.plot(x,y,'y^') #use of different colors/design for nodes

for i in range(n): #create connections between nodes
    for j in range(i):
           if matrix[i][j]==1:
                plt.plot([x[i],x[j]],[y[i],y[j]],'m-') #use of different color/design for edges

plt.xlabel('Horizontal (x-axis)') #label for x-axis
plt.ylabel('Vertical (y-axis)') #label for y-axis
plt.title('Network of European Emails') #title
plt.show()