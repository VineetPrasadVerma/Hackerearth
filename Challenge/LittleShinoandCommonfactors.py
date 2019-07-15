import math
num_a, num_b = tuple(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


hcf = gcd(num_a, num_b)
divs = [1]
for i in range(2, int(math.sqrt(hcf)) + 1):
    if hcf % i == 0:
        divs.extend([i, hcf // i])
divs.extend([hcf])
#print(divs)
print(len(set(divs)))
