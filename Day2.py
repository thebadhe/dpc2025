'''
Problem : Find the Missing Number
You are given an array arr containing n-1 distinct integers. The array consists of integers taken from the range 1 to n, meaning one integer is missing from this sequence. Your task is to find the missing integer.

Input :
An integer array arr of size n-1 where the elements are distinct and taken from the range 1 to n.
Example : arr = [1, 2, 4, 5]

Output :
Return the missing integer from the array.
Example: Missing number: 3
'''

def find_missing(arr):
    n = len(arr)+1
    # pringt(n)
    exact_sum = n*(n+1)//2
    actual_sum = sum(arr)
    # print(exact_sum)
    # print(actual_sum)
    return exact_sum-actual_sum

input_arr = eval(input(""))
print("Missing Value: ",find_missing(input_arr))