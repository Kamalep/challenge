def fizzBuzz(n):
    for i in range(1, n + 1):
        fizz = 'Fizz' if multipleof(i, 3) else ''
        buzz = 'Buzz' if multipleof(i, 5) else ''
        print(f'{fizz}{buzz}' or i)

        # if multipleof(i, 3) and multipleof(i, 5):
        #     o = 'FizzBuzz'
        # elif multipleof(i, 3):
        #     o = 'Fizz'
        # elif multipleof(i, 5):
        #     o = 'Buzz'
        # else:
        #     o = str(i)
        # print(o)

def multipleof(n, x):
    return not bool(n % x)


fizzBuzz(25)
# print('multiply 3')
# print('6 =', fizzBuzz(6))
# print('9 =', fizzBuzz(9))
# print('12 =', fizzBuzz(12))
#
# print('multiply 5')
# print('10 =', fizzBuzz(10))
# print('25 =', fizzBuzz(25))
# print('35 =', fizzBuzz(35))
#
# print('multiply 5 and 3')
# print('15 =', fizzBuzz(15))
# print('30 =', fizzBuzz(30))
#
# print('Normal')
# print('59 =', fizzBuzz(59))
# print('77 =', fizzBuzz(77))
