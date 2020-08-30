"""
Joanne Kwon
PIC 16
Professor Cai
February 11, 2019
"""

'''
HOMEWORK 4 PROBLEM 2
matplotlibs was utilized to create a labeled histogram. The 2013-2015 NY Mathematics Exam dataset was found at:
https://catalog.data.gov/dataset/new-york-state-mathematics-exam/resource/edaa4f06-b2d8-470e-8dcf-23998a93fbe8
'''

import matplotlib.pyplot as plt
import pandas as pd

metadata=pd.read_table('2013-2015 NY Math Exam.csv') #reads csv file

score=metadata['Mean Scale Score'] #extract data for Mean Scale Score
bins=[260,270,280,290,300,310,320,330,340] #bin ranges

plt.hist(score,bins=bins,color='pink',edgecolor='black',linewidth=.5) #graphs histogram
plt.ylabel('Frequency of Scores')
plt.xlabel('Mean Scale Score') 
plt.title('2013-2015 NY State Mathematics Exam Scores')
plt.show()


