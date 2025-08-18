'''
Problem : Merge Two Sorted Arrays
You are given two sorted arrays arr1 of size m and arr2 of size n. Your task is to merge these two arrays into a single sorted array without using any extra space (i.e., in-place merging). The elements in arr1 should be merged first, followed by the elements of arr2, resulting in both arrays being sorted after the merge.

Input :
Two sorted integer arrays arr1 of size m and arr2 of size n.
Example : 
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

Output :
Both arr1 and arr2 should be sorted after the merge. Since you cannot use extra space, the final result will be reflected in arr1 and arr2.
Example:
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
'''

def mergeArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    merged = [0] * (n + m)

    for i in range(n):
        merged[i] = arr1[i]
    for j in range(m):
        merged[n + j] = arr2[j]

    merged.sort()
    # print("Sorted Merged Array: ", merged)
    for i in range(n):
        arr1[i] = merged[i]

    for j in range(m):
        arr2[j] = merged[n + j]
    print("Final arr1: ", arr1)
    print("Final arr2: ", arr2)

arr1 = eval(input('Enter first sorted array: '))
arr2 = eval(input('Enter second sorted array: '))

mergeArrays(arr1, arr2)
