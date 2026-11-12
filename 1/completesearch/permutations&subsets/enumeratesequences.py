
import sys
input = lambda: sys.stdin.readline().strip("\n")

def main():
    n, k = map(int, input().split())
    r = tuple(map(int, input().split()))
    out = []

    def check_val(idx, seq, total):
        if idx == n:
            if total % k == 0:
                out.append(" ".join(map(str, seq)))
        else:
            for i in range(1, r[idx] + 1):
                seq.append(i)
                check_val(idx + 1, seq, total + i)
                seq.pop()

    check_val(0, [], 0)
    print("\n".join(out))

main()


