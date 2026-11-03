import sys
input = lambda: sys.stdin.readline().rstrip("\n")

def fail():
  print("No")
  sys.exit()

word = input().rstrip()

if len(word) % 2 != 0:
  fail()

letters = set()

for i in range(1, len(word) + 1, 2):
  if word[i] != word[i - 1]:
    fail()
  elif word[i] in letters:
    fail()
  letters.add(word[i])

print("Yes")


# sets, functions