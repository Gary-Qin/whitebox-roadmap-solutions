import sys
input = lambda: sys.stdin.readline().strip("\n")

def main():
    n, m, x = map(int, input().split())
    books = []
    lowest_cost = 1200001
    
    for _ in range(n):
        books.append(tuple(map(int, input().split())))

    def is_levels_met(levels):
        for level in levels:
            if level < x:
                return False
        return True

    def increment_levels(levels, book_levels):
        for i in range(len(levels)):
            levels[i] += book_levels[i]

    def decrement_levels(levels, book_levels):
        for i in range(len(levels)):
            levels[i] -= book_levels[i]

    def search(books, levels, cost):
        nonlocal lowest_cost
        if is_levels_met(levels):
            lowest_cost = min(lowest_cost, cost)
        else:
            if books:
                book = books.pop()
                increment_levels(levels, book[1:])
                search(books, levels, cost + book[0])   # buy the book
                decrement_levels(levels, book[1:])
                search(books, levels, cost)             # skip the book
                books.append(book)   

    search(books, [0 for i in range(m)], 0)
    print(lowest_cost if lowest_cost <= 1200000 else -1)

main()
