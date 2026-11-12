import sys
input = lambda: sys.stdin.readline().rstrip("\r")

n = int(input())
input_nums = tuple(map(int, input().split()))
missing_nums = set(range(1, n + 1))

for num in input_nums:
  missing_nums.remove(num)

for value in missing_nums:
  print(value)

# used a set instead of a list