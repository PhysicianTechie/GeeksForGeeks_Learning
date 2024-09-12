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


#######################################################
#Python data types
#######################################################

######################################################

# python operators

##########################################################
