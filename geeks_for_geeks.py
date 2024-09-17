# geeks for geeks learning python
# Python class and Objects

# create class GFG and use init method to provide attributes name and company
class GFG:
    def __init__(self):
        self.name = 'name'
        self.company = 'geeksforgeeks'
        
    # create method show which will print 
    # name and company
    def show(self):
        print("Name is", self.name)
        print("Company is", self.company)

# create object obj of class GFG
obj = GFG()
obj.show()
print(obj.name)
print(obj.company)

#The below code shows how Python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(self.name)
        print(self.salary)
        
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def show(self):
        print(self.radius)
        
# creating objects of the Employee class
# and Circle class
list = [Employee('Geek', 100000), Circle(2)]
for obj in list:
    obj.show()


# polymorphism using inheritance and method overriding
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return self.name + ' says Woof!'
    
class Cat(Animal):
    def speak(self):
        return self.name + ' says Meow!'

fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())

# PYTHON ITERATORS

# A simple Python program to demonstrate
# working of iterators using an example type
# that iterates from 10 to given value

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += 1
        return current
    
# Driver code
nums = MyRange(10, 15)
for num in nums:
    print(num)


#Python exception handling
# Python program to handle simple runtime error
a = [1, 2, 3]
try:
    print("Second element = %d" %(a[1]))
    
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" %(a[3]))
except IndexError:
    print("An error occurred")
       
