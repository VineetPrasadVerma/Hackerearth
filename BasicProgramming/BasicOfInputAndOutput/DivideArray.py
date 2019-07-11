size = int(input())
arr = list(map(int, input().split()))
operations = int(input())
for i in range(operations):
    num = int(input())
    arr = [j//num for j in arr]


print(" ".join(str(i) for i in arr))