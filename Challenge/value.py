def solve(a):
    # Write your code here
    ans = 0
    for i in range(n, 0, -1):
        temp = 0

        for j in range(1, n+1):

            for k in range(n, 0, -1):

                if k>=i and i>=j and a[k-1]<a[i-1]:
                    temp += 1

        ans += temp//(i)

    return ans

n = int(input())
a = list(map(int, input().split()))

out_ = solve(a)
print(out_)