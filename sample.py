import pandas as pd
import numpy as np
print('welcome to git cloning tutorial')
a = 5
b = 6
c = 7

# Uncomment below to take inputs from the user
a = input('Enter first side: '))
b = float(input('Enter second side: '))
c = input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 0

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area
