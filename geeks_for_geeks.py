# geeks for geeks learning python

"""
print("hello world")

# commenting
# this is a comment in python
print("hello world")  # this is also a comment in python

# multiline comment

this is a
#multiline comment
in python

print("hello world")  # this is not a comment in python

# variable declaration
# in python we don't need to declare the type of variable before using it
x = 10  # here x is a variable of type integer
# print(x)  # this will print 10
# print(type(x))  # this will print <class 'int'>
# print(type("hello"))  # this will print <class 'str'>
# print(type(10.5))  # this will print <class 'float'>
# print(type(True))  # this will print <class 'bool'>
# print(type(None))  # this will print <class 'NoneType'>
# print(type([1, 2, 3]))  # this will print <class '
# print(type({"a": 1, "b": 2}))  # this will print
# <class 'dict'>
# print(type((1, 2, 3)))  # this will print <class '
# print(type({"a": 1, "b": 2}))  # this will print
# <class 'dict'>
# print(type({"a": 1, "b": 2}))  # this will print
# <class 'dict'>
# print(type({"a": 1, "b": 2}))  # this will print

# Python data types
x = 3j #complex
# create the list
my_list = [1, 2, 3, 4, 5]
# create the tuple
my_tuple = (1, 2, 3, 4, 5)
# create the dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
#create set
my_set = {1, 2, 3, 4, 5}

val = input("enter your value : ")
print(val)

# python if else
i = 20
if (i < 15):
            print("i is less than 15")
            print("i'm in if block")
else:
            print("i is greater than 15")
            print("i'm outside the else block")
print("i'm outside the if else block")


for i in range (0,10,2):
            print(i)





def evenOdd(x):
            if x % 2 == 0:
                        return "Even"
            else:
                        return "Odd"

print (evenOdd(2))
print (evenOdd(5))

print(evenOdd(12))
print(evenOdd(8))

"""
### ######################################
# Getting Started with Python Programming
###########################################
# SYNTAX
# dont need to declare variable's type explicitly,python will dynamically determine type.

#variables in python

# numbers

"""
#python string

string1 = '''Geeks
For
Life'''
print("\nCreating a multiline string: ")
# print the string

print(string1)

#moving on to next topic on string
#Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.

gfg = "GeeksforGeeks"
#program to reverse string

print("Original String:", gfg)
print("Reversed string:", gfg[::-1])

# use both list and string method to update the character
string1= "Hello, I'm a Geek"
print("Initial string: ")
print(string1)

#updating the character of a string using list method

string1_list = list(string1)
string1_list[7] = 'g'
string1 = ''.join(string1_list)
print("Updated string: ")
print(string1)          


# use slicing method to delete the character at 2nd Index

string2 = "Hello, I'm a Geek"
print("Original string: ")
print(string2)

# deleting the character at 2nd index using slicing method

string2 = string2[:2] + string2[3:]
print("Updated string: ")
print(string2)


# python string formatting using format() method

name = "GeeksforGeeks"
age = 21
print("Hello, my name is {0} and I am {1} years old".format(name, age))
"""

# 7 Sep 2024
# Variables continued...
# lists
#create a list
'''
my_list = [1, 2, 3, 4, 5]

# access the elements of the list

print(my_list[0])  # this will print 1
print(my_list[1])  # this will print 2
print(my_list[2])  # this will print 3
print(my_list[3])  # this will print 4
print(my_list[4])  # this will print 5

#getting size of the list

print(len(my_list))  # this will print 5

#complexities for accessing elements in a lists
#accessing an element in a list using index is O(1)
#accessing an element in a list using index is O(n)
#accessing an element in a list using index is O(n)
#accessing an element in a list using index is O(n)

string = input("enter the elements (space seperated): ")

#made some changes to gitlens settings for easy access to github

# here are some more changes
# split the string and store it to a list
lst = string.split()
print('The list is: ',lst)

####
# print the numbers from 0 to 4 using range and in single line.

for i in range(5):
            print(i, end=' ')
print()

# please crate class CSStudent with stream cse and objects 101 and 102

class CSStudent:
            def __init__(self, name, roll_no, stream, course1, course2):
                        self.name = name
                        self.roll_no = roll_no
                        self.stream = stream

'''

#####################################################
#Learn Python Input/Output
###################################################
# build a countdown timer like 5>4>3>2>1
import time
'''
for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
print("blast off!")

'''
# taking multiple inputs from user in python

'''
#######################################################
#Python data types
#######################################################

######################################################

# python operators

##########################################################
# how to access the elements of the string

# string slicing with example
##########################################################
'''
#Python conditional statement


# python loops
###########################################################\

# Python Functions
'''
def fun():
            print("welcome to geeksforgeeks")
            print("function is defined")
fun()

# create a function to add two numbers
def add(a, b):
            return a + b
print(add(2, 3))
''' 
'''
# create a function to determine if given number is prime or not

def is_prime(n):
            if n <= 1:
                        return False
            for i in range(2, n):
                        if n % i == 0:
                                    return False
            return True
print(is_prime(5))
print(is_prime(6))
'''

#########################################################


# solving some problems from geeksforgeeks
# Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.
'''
def subarray_sum(arr, s):
            n = len(arr)
            result = [-1, -1]
            curr_sum = 0
            start = 0
            for i in range(n):
                        curr_sum += arr[i]
                        while curr_sum > s:
                                    curr_sum -= arr[start]
                                    start += 1
                        if curr_sum == s:
                                    result = [start + 1, i + 1]
                                    break
            return result

# test the function
arr = [1, 2, 3, 7, 5]
s = 12
print(subarray_sum(arr, s))

#Given two Arrays A[] and B[] of length N and M respectively. Find the minimum number of insertions and deletions on the array A[], required to make both the arrays identical.Note: Array B[] is sorted and all its elements are distinct, operations can be performed at any index not necessarily at end.

def min_operations(A, B):
            n = len(A)
            m = len(B)
            i = j = count = 0
            while i < n and j < m:
                        if A[i] == B[j]:
                                    i += 1
                                    j += 1
                        else:
                                    count += 1
                                    i += 1
            count += n - i
            return count

# test the function
A = [1, 2, 3, 5, 1]
B = [1, 3, 5]
print(min_operations(A, B))


#Given a number num, our task is to find the closest Palindrome number whose absolute difference with the given number is minimal. If 2 Palindrome numbers have the same absolute difference as the given number, take the smaller one.

def nearest_palindrome(num):
    """
    Find the nearest palindrome number to the given number.

    Args:
        num (int): The input number.

    Returns:
        int: The nearest palindrome number.
    """
    num_str = str(num)
    num_len = len(num_str)

    # Handle even-length palindromes
    if num_len % 2 == 0:
        left_half = num_str[:num_len // 2]
        right_half = left_half[::-1]
        palindrome = int(left_half + right_half)
        if palindrome < num:
            palindrome = int(left_half + str(int(left_half) + 1)[::-1])

    # Handle odd-length palindromes
    else:
        left_half = num_str[:num_len // 2]
        middle = num_str[num_len // 2]
        right_half = left_half[::-1]
        palindrome = int(left_half + middle + right_half)
        if palindrome < num:
            if middle == '9':
                left_half = str(int(left_half) + 1)
                palindrome = int(left_half + '0' + left_half[::-1])
            else:
                palindrome = int(left_half + str(int(middle) + 1) + left_half[::-1])

    return palindrome

# Test the function
num = 123
print(nearest_palindrome(num))


'''
#################################################################################

#PYTHON OOP CONCEPTS
'''
#################################################################################
An object consists of:

State: It is represented by the attributes of an object. It also reflects the properties of an object.
Behavior: It is represented by the methods of an object. It also reflects the response of an object to other objects.
Identity: It gives a unique name to an object and enables one object to interact with other objects.
'''

# Create class Dog with attribute as mammal
# also access the class attributes
'''
class Dog:
    # class attribute
    species = "mammal"


    # instance attribute
    def __init__(self, name):
        self.name = name
        
#driver code
# instantiate the Dog class
philo = Dog("Philo")
mikey = Dog("Mikey")

# access the class attribute
print("Philo is a {}".format(philo.__class__.species))
print("Mikey is also a {}".format(mikey.__class__.species))

# access the instance attribute
print("{} is {}".format(philo.name, philo.species))
print("{} is {}".format(mikey.name, mikey.species))

# change the instance attribute
mikey.species = "reptile"

# access the changed instance attribute
print("{} is {}".format(mikey.name, mikey.species))


##########################################
# Python code to demonstrate how constructors are called create parent class Person and child class as Employee


# parent class
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print(self.name)
        print(self.idnumber)
        
# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

        # using super() method
        super().__init__(name, idnumber)

    def details(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling methods
a.display()
a.details()

##################################################################

#Polymorphism in Python
#demonstrate with class bird
class Bird:
    def intro(self):
        print("There are many types of birds.")
        
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")
        
#create class ostrich
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
        
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

'''
####################################################################################


