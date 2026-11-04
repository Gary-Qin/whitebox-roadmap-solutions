import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().strip()

n, q = map(int, input().split())
heights = sorted(map(int, input().split()))

for _ in range(q):
    height_threshold = int(input())
    print(n - bisect_left(heights, height_threshold))

# sorted is n*log(n)
# bisect_left for <, n - bisect_left for >=
# bisect_right for <=, n - bisect_right for >
# bisect_right - bisect_left to find the # of instances of a value in a sorted list; would be log(n)