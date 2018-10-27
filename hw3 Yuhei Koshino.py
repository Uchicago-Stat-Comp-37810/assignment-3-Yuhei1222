{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test for Exercise 1\n",
      "True\n",
      "False\n",
      "This in not divisible\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "# Name:Yuhei Koshino\n",
    "# hw3.py\n",
    "import math # Import math symbol\n",
    "import random # Import Random number generator \n",
    "##### Homework 3, exercises 1 -  ######\n",
    "\n",
    "\n",
    "# ********** Exercise 1 ********** \n",
    "\n",
    "# Define is_divisible function here\n",
    "\n",
    "def is_divisible(m,n): # Defining the function of is_divisible,which takes m,n as parameter. \n",
    "    if n == 0 : # If n = 0 \n",
    "        print(\"This in not divisible\") # then print the message. \n",
    "        return False\n",
    "    if (m % n) == 0: # If m is divisible by n, \n",
    "        return True # return true.\n",
    "    else:\n",
    "        return False # If m is not divisible by n, then return false. \n",
    "    \n",
    "# Test cases for is_divisible\n",
    "## Provided for you... uncomment when you're done defining your function\n",
    "print(\"Test for Exercise 1\")\n",
    "print(is_divisible(10, 5))  # This should return True\n",
    "print(is_divisible(18, 7))  # This should return False\n",
    "print(is_divisible(42, 0)) # What should this return? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test for Exercise 2\n",
      "True\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# ********** Exercise 2 ********** \n",
    "def not_equal(a,b): # define the function called \"not_equal\", which takes two parameters.\n",
    "    if a==b: # if two parameters are equal, \n",
    "        return False # then return false\n",
    "    else: # If not,\n",
    "        return True # return true\n",
    "\n",
    "\n",
    "# Test cases for not_equal\n",
    "print(\"Test for Exercise 2\")\n",
    "print(not_equal(1,2))\n",
    "print(not_equal(1,1))\n",
    "print(not_equal(1,10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test for multadd function\n",
      "10\n",
      "sin(pi/4) + cos(pi/4)/2 is:1.0606601717798212\n",
      "ceiling(276/19) + 2 log_7(12) is:17.55397881653925\n"
     ]
    }
   ],
   "source": [
    "# ********** Exercise 3 ********** \n",
    "\n",
    "## 1 - multadd function\n",
    "def multadd(a,b,c): # Defining the function called multadd, which takes 3 parameters\n",
    "    return(a * b + c) # return the value of a*b+c\n",
    "\n",
    "print(\"Test for multadd function\") # print\n",
    "print(multadd(2,3,4)) # print the result of multadd(2,3,4)\n",
    "\n",
    "## 2 - Equations\n",
    "angle_test = multadd((math.cos(math.pi/4)), 1/2, math.sin(math.pi/4)) \n",
    "ceiling_test = multadd(2, math.log(12,7), math.ceil(276/19))\n",
    "\n",
    "# Test Cases\n",
    "print (f\"sin(pi/4) + cos(pi/4)/2 is:{angle_test}\")\n",
    "print(f\"ceiling(276/19) + 2 log_7(12) is:{ceiling_test}\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The number is 88\n",
      "The number is divisible by 3 : False\n"
     ]
    }
   ],
   "source": [
    "# ********** Exercise 4 **********\n",
    "\n",
    "def rand_divis_3():  #Takes no parameter\n",
    "    h = random.randint(0,100)  #Generates a random number, 0 is minimum and 100 is maximum\n",
    "    if(h%3 == 0):   #True Condition : the remainder of a by 3 is equal to zero.\n",
    "        print(f\"The number is {h}\") #Print the random number\n",
    "        return True\n",
    "    else:\n",
    "        print(f\"The number is {h}\") # Print the random number if it is not divisible by 3.\n",
    "        return False\n",
    "\n",
    "# Test Cases\n",
    "print(f\"The number is divisible by 3 : {rand_divis_3()}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
