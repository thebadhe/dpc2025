
def leaders(arr):
    result = []
    n = len(arr)
    
    for i in range(n):

        for j in range(i + 1, n):
        
            if arr[i] < arr[j]:
                break
        else:

            result.append(arr[i])
    
    return result


arr = [16, 17, 4, 3, 5, 2]
result = leaders(arr)
print(" ".join(map(str, result)))