# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

def zeros():
    return np.arange(0, 10)

def multiply(str):
    str = "whole lotta " + str  
    return str

def multiply2(i):
    i = "At least %d STACKS" % i  
    return i
    
if __name__ == "__main__":
    print("hello anaconda")
    
    Z = np.zeros(10)
    print(Z)
    print("%d bytes" % (Z.size * Z.itemsize))
    
    Z = np.zeros((10,10))
    print(Z)
    print("%d bytes" % (Z.size * Z.itemsize))
    
    Z = zeros()
    print(Z)
    print("%d bytes" % (Z.size * Z.itemsize))
    
    user_input = input("Bitch what you want (string have it in quotes): ") 
    try:
       val = int(user_input)
       print("Yes input string is an Integer.")
       print("Input number value is: ", val)
       str = multiply2(val)
    except ValueError:
       print("That's not an int!")
       print("No.. input string is not an Integer. It's a string")
       str = multiply(user_input)
       
    print ("Output:")
    print str
    
    # setup fibonacci function
    # import matplotlib as plt for visualizing data
    # learn how to use multiple python files