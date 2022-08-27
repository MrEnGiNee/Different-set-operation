# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 23:06:57 2022

@author: Abhinay Gautam
"""

# Program to perform different set operations like in mathematics

# define two sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)