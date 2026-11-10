import sys
input = lambda: sys.stdin.readline().strip("\n")

n = int(input())
s = input()
combos = 0

for d1 in range(10):
  for d2 in range(10):
    for d3 in range(10):
      has_d1 = s.find(str(d1))
      if has_d1 == -1:
        continue
      has_d2 = s.find(str(d2), has_d1 + 1)
      if has_d2 == -1:
        continue
      has_d3 = s.find(str(d3), has_d2 + 1)
      if has_d3 == -1:
        continue
      combos += 1

print(combos)
