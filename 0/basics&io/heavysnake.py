import sys
input = sys.stdin.readline

n, d = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(n)]

for k in range(d):
    heaviest = 0
    for t, l in pairs:
        weight = t * (l + k + 1)
        if weight > heaviest:
            heaviest = weight
    print(heaviest)


# sys.stdin.readline to replace input()
# map, tuple, x for _ in range(y)
