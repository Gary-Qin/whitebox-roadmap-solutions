import sys
input = sys.stdin.readline

n = int(input())
vals = tuple(map(int, input().split()))

for i in range(2, n):
  if vals[i] * vals[0] != vals[i - 1] * vals[1]:
    print("No")
    sys.exit()

print("Yes")

# float-point precision errors when comparing divisors, opt to cross-multiply and compare products instead