def multiply_and_filter(seq, multiplier):
    l = []
    lm = []
    l = list(filter(isn, seq))
    print(l)


def isn(e):
    if type(e) in (int, float):
        str.isdigit()
        return e

print(multiply_and_filter([1,2,None,[],'kamal',3,4], 1.5))
# print(multiply_and_filter([1,2,3,4], 1.5), [1.5, 3, 4.5, 6])
# print(multiply_and_filter([1,2,3], 0), [0, 0, 0])
# print(multiply_and_filter([0,0,0], 2), [0, 0, 0])
# print(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, []], 3), [3,7.5,30])
# print(multiply_and_filter([1, None, lambda x: x, 2.5, 'string', 10, None, {}, [], True, False], 3), [3,7.5,30])
