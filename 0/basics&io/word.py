import sys
input = sys.stdin.readline

word = input()
uppercase = 0
lowercase = 0

for char in word:
  if char.isupper():
    uppercase += 1
  elif char.islower():
    lowercase += 1

if uppercase > lowercase:
  print(word.upper())
else:
  print(word.lower())

# iterate chars in word
# char.isupper(), char.islower()
# str.upper(), str.lower()