# solving Geeks for Geeks problems

############
# trying basic questions first
##############

#Given two arrays, write a python function to return the intersection of the two. For example, X = [1,5,9,0] and Y = [3,0,2,9] it should return [9,0]
import numpy as np
x = np.array([1,5,9,0])

y = np.array([3,0,2,9])

intersection = np.intersect1d(x, y)

print(intersection)

# next question
#Define tuples and lists in Python What are the major differences between them?

#Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).
'''
def find_peak_element(arr):
    n = len(arr)
    
    # Check if the first element is a peak
    if n == 1 or arr[0] >= arr[1]:
        return 0
    
    # Check if the last element is a peak
    if arr[n-1] >= arr[n-2]:
        return n-1
    
    # Check for every other element
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i

# Test the function
arr1 = [1, 3, 20, 4, 1, 0]
arr2 = [1,10,12,4,7,17,45,456]
print(find_peak_element(arr1))# Output: 2
print(find_peak_element(arr2))

#another way of solving this using class
class Solution:   
    def peakElement(self,arr, n):
                # Check if the first element is a peak
                if n == 1 or arr[0] >= arr[1]:
                    return 0
                
                # Check if the last element is a peak
                if arr[n-1] >= arr[n-2]:
                    return n-1
                
                # Check for every other element
                for i in range(1, n-1):
                    if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
                        return i
            
# Test the function

s = Solution()
arr1 = [1, 3, 20, 4, 1, 0]
arr2 = [1,10,12,4,7,17,45,456]
print(s.peakElement(arr1, len(arr1)))# Output: 2
print(s.peakElement(arr2, len(arr2)))

'''




