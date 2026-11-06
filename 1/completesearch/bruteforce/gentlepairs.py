import sys
input = lambda: sys.stdin.readline().strip("\n")

n = int(input())
pairs = [tuple(map(int, input().split())) for i in range(n)]
in_range_slopes = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if pairs[j][0] - pairs[i][0] == 0:
            continue
        slope = (pairs[j][1] - pairs[i][1]) / (pairs[j][0] - pairs[i][0])
        if slope >= -1 and slope <= 1:
            in_range_slopes += 1

print(in_range_slopes)
