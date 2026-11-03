import sys
input = lambda: sys.stdin.readline().rstrip("\n")

n = int(input())
vals = tuple(map(int, input().split()))
product = 1

for val in vals:
  if val == 0:
    print("0")
    sys.exit()
  product *= val
  if product > 10 ** 18:
    if 0 in vals:
      print("0")
    else:
      print("-1")
    sys.exit()

print(product)

# edge case noob trap