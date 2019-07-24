def FindCost(C, Height, N):
    Height = list(Height)
    C = list(C)
    total_cost = 0
    for i in range(N-1):
        if Height[i]>=Height[i+1]:
            total_cost += 0
        else:
            total_cost += C[i]
    return total_cost

# Write your code here


N = int(input())

Height = map(int, input().split())
C = map(int, input().split())

out_ = FindCost(C, Height, N)
print(out_)