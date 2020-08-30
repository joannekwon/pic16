"""
Joanne Kwon
PIC 16
Professor Hanqin
January 18, 2019
"""

'''
PROBLEM 1
The function largerIndex(c) takes an input of a list of integers and returns 
a new list composed of 1, 0, or -1 based on the conditions that the value within
the list is greater than, equal to, or less than the value of its corresponding indicie.
'''
def largerIndex(c):
    k=[] #new list
    l=len(c) #length of inputted list
    for i in range(l):
        if c[i]>i: #value is greater than indicie
            k.append(1) #append 1 to new list k
        elif c[i]==i: #value is equal to the indicie
            k.append(0) #append 0 to new list k
        elif c[i]<i: #value is less than indicie
            k.append(-1) #append -1 to new list k
    return k

c=[8,1,98,-3,-4,9] #trial case
largerIndex(c)


'''
PROBLEM 2
The function squareUpTo(n) takes an input of a positive integer and returns a list 
square numbers up to the input integer.
'''
def squareUpTo(n):
    s_list=[] #list for square numbers
    s_int=1 #sub-integer
    i_int=1 #increment integer
    while n>=s_int: #while integer is less than or equal to input value run loop
        s_list.append(s_int) #values after 1 (1^2=1) are squared and added to the list
        i_int+=1
        s_int=i_int**2 #square new integer's (incremented by 1) value
    return s_list

squareUpTo(25) #trial case


'''
PROBLEM 3
The function fliplin3() uses fair coins to generate a biased coin with a success 
probability of 1/3.
'''
import random
val1=[]
val2=[]
val3=[]

def fliplin3():
    #component 1
    for i in range(3):
        val1.append(random.randint(0,1)) #append 3 random values (0 or 1) to list val1
    first=sum(val1) #add values in list val1
    #if sum equals 1, then 1, anyother 0
    #makes first probability of 3/8 (37.5)
    if first==1:
        first=1
    else:
        first=0

    #component 2
    for k in range(3):
        val2.append(random.randint(0,1)) #append 3 random values (0 or 1) to list val2
    second=sum(val2) #add values in list val2
    #if sum of val2 is true, then 1, anyother 1
    #makes second a probability of of 8/8 (1.0)
    if second is False:
        second=1
    else:
        second=1

    #component 3
    #third holds probability of 1/8 (12.5)
    for j in range(3):
        val3.append(random.randint(0,1)) #append 3 random values (0 or 1) to list val3
    third=reduce(lambda x,y:x*y,val3) #multiply values in list val3

    #calculation of probability 1/3, return prob of either 0 or 1 based on prob value
    prob=first/(second+third)
    if prob==1/2:
        prob=0
    return prob

fliplin3() #call function fliplin3


'''
PROBLEM 4
The function duplicates(c) takes an input of a list of integers where the
value's indice is greater than or equal to 1 and less than or equal to the
size of the list. The function lists the values that appear twice from the
input list, while preserving the original order of the values.
'''
def duplicates(c):
    output=[] #list for values that appear twice
    n=len(c) #length of inputted list
    for i in range(n):
        p1=i+1 #increment of 1 per loop, use for range of following loop
        for j in range(p1,n):
            #if value of lists are equal in value
            #if 1 is less than or equal to value from list
            #if value from list are less than or equal to length of list 
            if c[i]==c[j] and 1<=c[i] and c[i]<=n:
                output.append(c[i]) #append value to output list
    return output

c=[0,5,89,5,4,89,-2,4,-2,1,0] #trial case
duplicates(c)


'''
PROBLEM 5
The function longestpath(d) takes an input in a dictionary and determines 
the length of the longest path, counting each key to value as one step.
'''
def longestpath(d):
    output=0
    new_d=dict() #new dictionary
    for key in d:
        count=0
        val=key
        new_d[key]=d[key] #new_d set to val of d
        while val in d:
            try: #test for KeyError
                val=d[val] #val set to val of d
                count+=1 #append count by 1 for every loop
                if new_d[key]==d[val]: #if key in new_d is equal to value in input, then there's a path
                    break
            except KeyError: #handles KeyError after test
                break
        #output set equal to count if less than count, returning path output
        if count>output:
            output=count
    return output

d={'a':'b','b':'c','f':'g','g':'h','h':'a'} #trial case
longestpath(d)

