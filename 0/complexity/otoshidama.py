import sys
input = lambda: sys.stdin.readline().strip()

n, y = map(int, input().split())

for ten_ks in range(n + 1):
    five_ks = (-1000 * n - 9000 * ten_ks + y) / 4000
    one_ks = (5000 * n + 5000 * ten_ks - y) / 4000
    if five_ks >= 0 and one_ks >= 0 and five_ks.is_integer() and one_ks.is_integer():
        print(ten_ks, int(five_ks), int(one_ks))
        sys.exit()

print("-1 -1 -1")

# float.is_integer()