import sys

data = sys.stdin.buffer.read().split()

n = int(data[0])
print(len(set(data[1:n+1])))

# sys.stdin.buffer.read()
