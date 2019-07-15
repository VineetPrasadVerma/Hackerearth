size = int(input())
arr = list(map(int, input().split()))
sum_of_arr = sum(arr)
sorted_arr = sorted(arr)
for i in range(1, sorted_arr[-1]+1):
    if i*size > sum_of_arr:
        print(i)
        break
