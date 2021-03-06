#!/usr/bin/env python
# coding: utf-8

# Here you have a collection of guided exercises for the first class on Python. <br>
# The exercises are divided by topic, following the topics reviewed during the theory session, and for each topic you have some mandatory exercises, and other optional exercises, which you are invited to do if you still have time after the mandatory exercises. <br>
# 
# Remember that you have 5 hours to solve these exercises, after which we will review the most interesting exercises together. If you don't finish all the exercises, you can work on them tonightor tomorrow. 
# 
# At the end of the class, we will upload the code with the solutions of the exercises so that you can review them again if needed. If you still have not finished some exercises, try to do them first by yourself, before taking a look at the solutions: you are doing these exercises for yourself, so it is always the best to do them your way first, as it is the fastest way to learn!

# **Exercise 1.3 (🌶️):** You look at the clock and see that it is currently 14.00h. You set an alarm to go off 535 hours later. At what time will the alarm go off? Write a program that prints the answer. Hint: for the best solution, you will need the modulo operator. Second hint: The answer is 21.00h, but of course, this exercise is not about the answer, but about how you get it.

# In[1]:


#Your Code Here
cur_time = 14.0
alarm_time = 535
ring_alarm = (cur_time) + (alarm_time%24)
print(f"Alarm goes off at {ring_alarm}")


# **Exercise 5.4 (🌶️):** "99 bottles of beer" is a traditional song in the United States and Canada. It is popular to sing on long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's simple lyrics are as follows: "99 bottles of beer on the wall, 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall." The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach zero. Write a function that generates and prints all the verses of the song (though you might start a bit lower, for instance with 10 bottles). Make sure that your loop is not endless, and that you use the proper inflection for the word "bottle".

# In[4]:


#Your Code Here
def beersong(n):
    while n > 0:
        """
        5 bottles of beer on the wall, 5 bottles of beer. Take one down, pass it around, 4 bottles of beer in the wall
        4 bottles of beer on the wall, 4 bottles of beer. Take one down, pass it around, 3 bottles of beer in the wall
        3 bottles of beer on the wall, 3 bottles of beer. Take one down, pass it around, 2 bottles of beer in the wall
        2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around, 1 bottle of beer in the wall
        1 bottle of beer on the wall, 1 bottle of beer. Take one down, pass it around, 0 bottles of beer in the wall
        """
        print(f"{n} bottles of beer on the wall, {n} bottles of beer. Take one down, pass it around, {n-1} bottles of beer in the wall")
        n -= 1
    return
beersong(5)


# **Exercise 5.5 (🌶️):** The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a function that calculates and prints the Fibonacci sequence until the numbers get higher than a `maximum`.

# In[43]:


#Your Code Here
def fibonacci():
    """
    Fibonacci sequence up to 22 :
    0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21
    """
    i,t = 0,1
    f = 0
    while f < 8:
        print(i)
        n = i + t
        i = t
        t = n
        f += 1

    return 
fibonacci()


# **Exercise 5.8 (🌶️):** A, B, C, and D are all different digits. The number DCBA is equal to 4 times the number ABCD. What are the digits? Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero. Use a quadruple-nested loop.

# In[ ]:


#Your Code Here
# Solve 4*ABCD == DCBA
def nested_nest():
    
    """
    A = 2
    B = 1
    C = 7
    D = 8
    """
    
    return
    

