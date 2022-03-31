#
# Balanced Number (Special Numbers Series #1 )   : 7 kyu
# Balanced number is the number that * The sum of all digits to the left of the middle digit(s)
# and the sum of all digits to the right of the middle digit(s) are equal*.


def sumside(s):
    total = 0
    for i in s:
        total += int(i)
    return total


def balanced_num(n):
    s = str(n)
    l = len(s)

    if l < 3: return "Balanced"

    middle = int(l / 2)
    right = left = 0

    if l % 2:
        right = sumside(s[:middle])
        left = sumside(s[middle + 1:])
    else:
        right = sumside(s[:middle - 1])
        left = sumside(s[middle + 1:])

    return "Balanced" if left == right else "Not Balanced"


# balanced_num(7)  , "Balanced");
# balanced_num(959), "Balanced");
# balanced_num(13) , "Balanced");
# balanced_num(432), "Not Balanced");
# balanced_num(424), "Balanced");

print(balanced_num(7))
print(balanced_num(959))
print(balanced_num(13))
print(balanced_num(432))
print(balanced_num(424))
