'''Using inbuilt function'''
# ip = [0,1,2,1,0,2,1,0]
# o/p :- [0,0,0,1,1,1,2,2]
# ip.sort()
# print(ip)

'''using swapping'''
def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = eval(input("Enter the values: "))
n = len(arr)
sortArray(arr)
print("After sorting:")
print(arr)

