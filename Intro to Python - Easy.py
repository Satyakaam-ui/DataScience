#!/usr/bin/env python
# coding: utf-8

# Here you have a collection of guided exercises for the first class on Python. <br>
# The exercises are divided by topic, following the topics reviewed during the theory session, and for each topic you have some mandatory exercises, and other optional exercises, which you are invited to do if you still have time after the mandatory exercises. <br>
# 
# Remember that you have 5 hours to solve these exercises, after which we will review the most interesting exercises together. If you don't finish all the exercises, you can work on them tonightor tomorrow. 
# 
# At the end of the class, we will upload the code with the solutions of the exercises so that you can review them again if needed. If you still have not finished some exercises, try to do them first by yourself, before taking a look at the solutions: you are doing these exercises for yourself, so it is always the best to do them your way first, as it is the fastest way to learn!

# **Exercise 1.1:** The cover price of a book is 24.95 EUR, but bookstores get a 40 percent discount. Shipping costs 3 EUR for the first copy and 75 cents for each additional copy. **Calculate the total wholesale costs for 60 copies**. 

# In[1]:


#Your Code Here
book_cost = 24.95
discount = 40
book_price_after_disc = book_cost - (book_cost*(discount/100))
wholesale_price = ((book_price_after_disc + 3) +((book_price_after_disc + 0.75) * 59))
print(wholesale_price)


# **Exercise 1.2:** When something is wrong with your code, Python will raise errors. Often these will be "syntax errors" that signal that something is wrong with the form of your code (e.g., the code in the previous exercise raised a `SyntaxError`). There are also "runtime errors", which signal that your code was in itself formally correct, but that something went wrong during the code's execution. A good example is the `ZeroDivisionError`, which indicates that you tried to divide a number by zero (which, as you may know, is not allowed). Try to make Python **raise such a `ZeroDivisionError`.**

# In[2]:


#Your Code Here
sample_var = 5/0
sample_var + 5


# **Exercise 5.1**: Create a countdown function that starts at a certain count, and counts down to zero. Instead of zero, print "Blast off!". Use a `for` loop. 
# 

# In[6]:


# Countdown
def countdown(time):
    """
    20
    19
    18
    17
    16
    15
    14
    13
    12
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    Blast off!
    """
    i = time
    while i >= 0 :
        if i == 0:
            print("Blast off!")
        else:
            print(i)
        i -= 1
    return
countdown(20)


# **Exercise 5.2:** Write and test three functions that return the largest, the smallest, and the number of dividables by 3 in a given collection of numbers. Use the algorithm described earlier in the Part 5 lecture :)

# In[ ]:


# Your functions
def main()
    """
    a = [2, 4, 6, 12, 15, 99, 100]
    100
    2
    4
    """
    return