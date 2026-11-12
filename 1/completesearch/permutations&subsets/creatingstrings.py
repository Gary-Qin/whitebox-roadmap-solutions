import sys
import string
input = lambda: sys.stdin.readline().strip("\n")

def main():
    counts = {}
    letters = input()
    for letter in letters:
        counts[letter] = counts.get(letter, 0) + 1

    perms = []

    def search(seq):
        if len(seq) == len(letters):
            perms.append("".join(seq))
        else:
            for letter in string.ascii_lowercase:
                if counts.get(letter, 0) > 0:
                    counts[letter] -= 1
                    seq.append(letter)
                    search(seq)
                    seq.pop()
                    counts[letter] += 1

    search([])

    print(len(perms))
    print("\n".join(perms))

main()