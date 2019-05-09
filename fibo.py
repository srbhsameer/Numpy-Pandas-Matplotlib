#!/usr/bin/env python
# coding: utf-8

# 2.3.3 Write a python module script that contains fib2() method to calculate the Fibonacci series till 1000 and save it as fibo.py.
# Note : The module created as fibo.py has to be placed in lib folder
# For linux/ubuntu path = /home/anaconda/lib/python3 For Windows path = C:\Users\Ajit\Anaconda3\Lib

# In[1]:


# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




