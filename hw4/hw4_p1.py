"""
Joanne Kwon
PIC 16
Professor Cai
February 11, 2019
"""

'''
HOMEWORK 4 PROBLEM 1
The function fnct(n) utilizes turtle to draw regular n-gons.
'''

import turtle as t

def ngon(n):
    for i in range(n):
        t.fd(20) #15 pixels in distance
        point=360/n #turns a degree of point (360 degrees divided by input of n)
        t.right(point) #move to the right based on point angle
    t.done()

n=8 #test case
ngon(n) #call function