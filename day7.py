'''
Problem : Trapping Rain Water
You are given an array height[] of non-negative integers where each element represents 
the height of a bar in a histogram-like structure. These bars are placed next to each other,
 and the width of each bar is 1 unit. When it rains, water gets trapped between the bars if 
 there are taller bars on both the left and right of the shorter bars. The task is to calculate 
 how much water can be trapped between these bars after the rain.

Input :
An integer array height[] where each element represents the height of a bar in the histogram.
Example : 
height[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
'''

def maxWater(arr):
    res = 0
    for i in range(1, len(arr) - 1):
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])
        right = arr[i]
        for j in range(i + 1, len(arr)):
            right = max(right, arr[j])
        res += (min(left, right) - arr[i])

    return res



arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxWater(arr))