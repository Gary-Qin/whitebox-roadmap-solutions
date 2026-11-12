num = int(input())
values = [num]

while num != 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = num * 3 + 1
    values.append(num)

print(*values)


# `//` for integer division
# `*` for unpacking (... in js)