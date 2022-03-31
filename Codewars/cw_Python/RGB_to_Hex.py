def rgb(r, g, b):
    # your code here :)
    r = roundto(r)
    g = roundto(g)
    b = roundto(b)
    return "{:02x}{:02x}{:02x}".format(r, g, b).upper()


def roundto(n):
    result = n
    if n < 0:
        result = 0
    elif n > 255:
        result = 255
    return result


print(rgb(0, 0, 0))  # ---> "000000"
print(rgb(1, 2, 3))  # ---> "010203"
print(rgb(255, 255, 255))  # ---> # ---> "FFFFFF"
print(rgb(254, 253, 252))  # ---> "FEFDFC"
print(rgb(-20, 275, 125))  # ---> "00FF7D"
