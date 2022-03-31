# K-CPU
def brain(x, y):
    if x.isnumeric():
        return x
    else:
        XY = y+x
        return int(eval(XY)) if x[0] == '/' else eval(XY)

# K-numbers
def zero(x='0', y='0'): return brain(x, y)
def one(x='1',y='1'): return brain(x, y)
def two(x='2', y='2'): return brain(x, y)
def three(x='3', y='3'): return brain(x, y)
def four(x='4', y='4'): return brain(x, y)
def five(x='5', y='5'): return brain(x, y)
def six(x='6', y='6'): return brain(x, y)
def seven(x='7', y='7'): return brain(x, y)
def eight(x='8', y='8'): return brain(x, y)
def nine(x='9', y='9'): return brain(x, y)

# K-operators
def plus(arg): return '+' + arg
def minus(arg): return '-' + arg
def times(arg): return '*' + arg
def divided_by(arg): return '/' + arg

print(seven(times(five())))  # 35
print(four(plus(nine())))  # 13)
print(eight(minus(three())))  # 5
print(six(divided_by(two())))  # 3


# def brain(x, y):
#     if x.isnumeric():
#         return x
#     else:
#         return int(eval(y + x)) if x[0] == '/' else eval(y + x)
#         # if x[0] == '/':
#         #     return int(eval(y + x))
#         # else:
#         #     return eval(y + x)
#
# # K-numbers
# def zero(x='0', y='0'): return brain(x, y)
# def one(x='1',y='1'): return brain(x, y)
# def two(x='2', y='2'): return brain(x, y)
# def three(x='3', y='3'): return brain(x, y)
# def four(x='4', y='4'): return brain(x, y)
# def five(x='5', y='5'): return brain(x, y)
# def six(x='6', y='6'): return brain(x, y)
# def seven(x='7', y='7'): return brain(x, y)
# def eight(x='8', y='8'): return brain(x, y)
# def nine(x='9', y='9'): return brain(x, y)
#
# # K-operators
# def plus(arg): return '+' + arg
# def minus(arg): return '-' + arg
# def times(arg): return '*' + arg
# def divided_by(arg): return '/' + arg
#

# def zero(exp='0'):
#     if exp.isnumeric():
#         return '0'
#     else:
#         if exp[0] == '/':
#             return int(eval('0' + exp[0] + exp[1]))
#         else:
#             return eval('0' + exp[0] + exp[1])
#
#
# def one(exp='1'):
#     if exp.isnumeric():
#         return '1'
#     else:
#         if exp[0] == '/':
#             return int(eval('1' + exp[0] + exp[1]))
#
#         else:
#             return eval('1' + exp[0] + exp[1])
#
#
# def two(exp='2'):
#     if exp.isnumeric():
#         return '2'
#     else:
#         if exp[0] == '/':
#             return int(eval('2' + exp[0] + exp[1]))
#
#         else:
#             return eval('2' + exp[0] + exp[1])
#
#
# def three(exp='3'):
#     if exp.isnumeric():
#         return '3'
#     else:
#         if exp[0] == '/':
#             return int(eval('3' + exp[0] + exp[1]))
#
#         else:
#             return eval('3' + exp[0] + exp[1])
#
#
# def four(exp='4'):
#     if exp.isnumeric():
#         return '4'
#     else:
#         if exp[0] == '/':
#             return int(eval('4' + exp[0] + exp[1]))
#
#         else:
#             return eval('4' + exp[0] + exp[1])
#
#
# def five(exp='5'):
#     if exp.isnumeric():
#         return '5'
#     else:
#         if exp[0] == '/':
#             return int(eval('5' + exp[0] + exp[1]))
#
#         else:
#             return eval('5' + exp[0] + exp[1])
#
#
# def six(exp='6'):
#     if exp.isnumeric():
#         return '6'
#     else:
#         if exp[0] == '/':
#             return int(eval('6' + exp[0] + exp[1]))
#
#         else:
#             return eval('6' + exp[0] + exp[1])
#
#
# def seven(exp='7'):
#     if exp.isnumeric():
#         return '7'
#     else:
#         if exp[0] == '/':
#             return int(eval('7' + exp[0] + exp[1]))
#
#         else:
#             return eval('7' + exp[0] + exp[1])
#
#
# def eight(exp='8'):
#     if exp.isnumeric():
#         return '8'
#     else:
#         if exp[0] == '/':
#             return int(eval('8' + exp[0] + exp[1]))
#
#         else:
#             return eval('8' + exp[0] + exp[1])
#
#
# def nine(exp='9'):
#     if exp.isnumeric():
#         return '9'
#     else:
#         if exp[0] == '/':
#             return int(eval('9' + exp[0] + exp[1]))
#
#         else:
#             return eval('9' + exp[0] + exp[1])
#
#
# def plus(s): return '+' + s
#
#
# def minus(s): return '-' + s
#
#
# def times(s): return '*' + s
#
#
# def divided_by(s): return '/' + s
#

