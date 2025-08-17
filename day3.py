'''
Problem : Find the Duplicate Number
You are given an array arr containing n+1 integers, where each integer is in the range [1, n] inclusive. 
There is exactly one duplicate number in the array, but it may appear more than once. 
Your task is to find the duplicate number without modifying the array and using constant extra space.

Input :
An integer array arr of size n+1, where each element is an integer in the range [1, n].
Example : arr = [3, 1, 3, 4, 2]

Output :
Return the duplicate integer present in the array.
Example: Duplicate number: 3
'''

def find_duplicate(arr):
    for i in arr:
        total=arr.count(i)
        # print(total)
        if total>1:
            return i


arr = eval(input('> '))
print("Dulpicate Number: ",find_duplicate(arr))