# -*- coding: utf-8 -*-
"""assignment5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HjZACkGHtHBMI_gyxqn166CYVbeq4xd-

1. Write a function to compute 5/0 and use try/except to catch the exceptions.
"""

def try_except():
    a=5 
    b=0
    try:
        d=a/b 
    except Exception as e:
        print("YOu cannot divide by zero")
try_except()
print()

"""1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.
"""

#1.2
l1=[]
def filter_long_words(l,n):
    for i in l:
        if(len(i)>n):
            l1.append(i)
    print(l1)

l=["hello","world","python","is","a ","programming","language"]
n=int(input("enter the integer "))
filter_long_words(l,n)

"""2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
"""

l1=[]
def map_len(l):
    for i in l:
        l1.append(len(i))
    print(l1)
l=["hello","world","python","is","a","programming","language"]
print(l)
map_len(l)

"""2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
"""

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
s=""
for i in subjects:
    for j in verbs:
        for k in objects:
            s=i+" "+j+" "+k
            print(s)