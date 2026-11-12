import sys
from itertools import combinations
input = lambda: sys.stdin.readline().strip("\n")

sum = 0
march_dict = {}
march_letters = ["M", "A", "R", "C", "H"]
for letter in march_letters:
    march_dict.setdefault(letter, 0)

n = int(input())
for _ in range(n):
    word = input()
    first_letter = word[:1]
    if first_letter in march_letters:
        march_dict[first_letter] += 1

for combo in combinations(march_letters, 3):
    product = 1
    for letter in combo:
        product *= march_dict[letter]
    sum += product

print(sum)
