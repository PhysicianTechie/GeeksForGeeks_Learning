# geeks for geeks learning python

# Python file handling
# File handling is an important part of web application.
# Python has several functions for creating, reading, updating, and deleting files.
# Python's file handling is based on the concept of a file object.
'''
# open the file command
# open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:

# open a file named geek in reading mode
f = open("geek.txt", "r")

# read the content of the file
print(f.read())

# now close the file
f.close()

# please provide example of user defined exception
# A user can create his own exception by creating a new exception class.
# This exception class has to be derived, either directly or indirectly, from Exception class.
# Most of the built-in exceptions are also derived from this class.
'''
class MyError(Exception):
    """This is a custom exception"""
    pass

def divide(x, y):
    if y == 0:
        raise MyError("Can't divide by zero")
    else:
        return x / y

try:
    divide(5, 0)
    


except MyError as e:
    print(e)
else:       
            print("Division successful")
finally:
            print("Program executed successfully")
            
