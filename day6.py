'''
Problem : Find All Subarrays with Zero Sum
You are given an integer array arr of size n. Your task is to find all the subarrays whose elements sum up to zero. 
A subarray is defined as a contiguous part of the array, and you must return the starting and ending 
indices of each subarray.

Input :
An integer array arr of size n where n represents the number of elements in the array.
Example : 
Input: [1, 2, -3, 3, -1, 2]

Output :
- Return a list of tuples, where each tuple contains two integers. The starting index (0-based) of 
the subarray. The ending index (0-based) of the subarray.
- The output should list all subarrays that sum to zero. If no such subarrays are found, 
return an empty list.
Example
Output: [(0, 2), (1, 3)]
'''



def findSubArrays(arr, n):

    hashMap = {}
    out = []
    sum1 = 0
    for i in range(n):
        sum1 += arr[i]
        if sum1 == 0:
            out.append((0, i))
        al = []

        if sum1 in hashMap:
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    return out

arr = [1, 2, -3, 3, -1, 2]
n = len(arr)
out = findSubArrays(arr, n)
print(out)