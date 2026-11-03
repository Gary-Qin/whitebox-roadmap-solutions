import sys
input = sys.stdin.readline

cards = tuple(map(int, input().split()))
card_count = {}

for card in cards:
  card_count[card] = card_count.get(card, 0) + 1

if len(card_count) != 2:
  print("No")
else:
  print("Yes")

# adding to dict


