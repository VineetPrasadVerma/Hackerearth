arr = [1,2,3,4,5,6]
prod = [0]*len(arr)
for i in range(0, len(prod)):
    temp = 1
    for j in range(0, len(arr)):
        if i != j:
            temp *= arr[j]
    prod[i] = temp

print(prod)