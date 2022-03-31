def calculator1(txt):
    dot = '.'
    x, op, y = txt.split()
    x, y = str(x.count(dot)), str(y.count(dot))
    return '.' * eval(x + op + y)


def calculator(txt):
    x, op, y = txt.split()
    x, y = len(x), len(y)
    d = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "//": x // y
    }
    return "." * d[op]


print(calculator("..... + ..............."))  # ----> "...................."
print(calculator("..... - ..."))  # ----> ".."
print(calculator("..... - ."))  # ----> "...."
print(calculator("..... * ..."))  # ----> "..............."
print(calculator("..... * .."))  # ----> ".........."
print(calculator("..... // .."))  # ----> ".."
print(calculator("..... // ."))  # ----> "....."
print(calculator(". // .."))  # ----> ""
print(calculator(". - ."))  # ----> ""
