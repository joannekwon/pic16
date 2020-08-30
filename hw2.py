"""
Joanne Kwon
PIC 16
Professor Cai
January 26, 2019
"""

'''
HOMEWORK 2
The solve function implements the Newton-Raphson method to find the root of a function. 
Our goal is to take a function, it's derivative, inital guess, and a desired tolerance in order 
o find the value x^* that is close to the root of the function, such that |f(x^*)|<= ε.
'''

import math #math library for values like exp, sin, cos, etc.

def solve(functions,guess,tolerance):
    if abs(functions(guess)[0])<=tolerance: #returns initial guess if abs error is less than or equal to tolerance
        return guess #returns if initial guess is close to the root
    else:
        while abs(functions(guess)[0])>tolerance: #updates guess until its abs error is less than tolerance
            guess=float(guess-functions(guess)[0]/functions(guess)[1]) #formula for Newton's Raphson method
        return guess

'''
TEST SOLVE FUNCTION
Use the solve function with the following f(x), f'(x), and x0.

print solve(lambda x:[x**2-1,2**x],3,0.0001) --> result: 1.00003544943
print solve(lambda x:[x**2-1,2*x],-1,0.0001) --> result: -1
print solve(lambda x:[math.exp(x)-1,math.exp(x)],1,0.0001) --> result: 1.5641107899e-06
print solve(lambda x:[math.sin(x),math.cos(x)],0.5,0.0001) --> result: 3.31180213264e-05
'''

'''
BONUS
Test the solve function with different tolerance values. How many iterations does it take to
find a desired approximation of the root? Can you find a pattern?

When testing the solve function with various tolerance values, the iteration quadratically 
converges (quadratic convergence) from the initial guess. Mathematically, the square of the error 
from one iteration is set proportionally to the following iteration error. This, therefore, 
approximately elicits a doubling pattern with each iteration, wherein which an error goes from 
a single digit to a double digit to a quadruple digit and continues on with a similar doubling pattern.
'''

