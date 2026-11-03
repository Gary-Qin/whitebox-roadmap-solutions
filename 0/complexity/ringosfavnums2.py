import sys
input = sys.stdin.readline

n = int(input())
vals = tuple(map(int, input().split()))
remainder_frequencies = {}
pairs = 0

for val in vals:
  remainder = val % 200
  remainder_frequencies[remainder] = remainder_frequencies.get(remainder, 0) + 1

for frequency in remainder_frequencies.values():
  if frequency >= 2:
    pairs += frequency * (frequency - 1) / 2

print(int(pairs))
