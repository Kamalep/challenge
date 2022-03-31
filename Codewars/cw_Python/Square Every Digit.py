def square_digits(num):
    r = [str(int(c) ** 2) for c in str(num)]
    r2 = list(map(lambda c: str(int(c) ** 2), r))
    return int(''.join(r))


def s(c):
    output = str(int(c) ** 2)
    return output


def square_digits1(num):
    return int(''.join([str(n * n) for n in map(int, str(num))]))


# print(square_digits(9119))
# print(square_digits(0))


def square_digits3(num):
    # r = list(map(lambda n: str(int(n) ** 2), str(num)))
    return int(''.join(map(lambda n: str(int(n) ** 2), str(num))))


print(square_digits3(9119))
