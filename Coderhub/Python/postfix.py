# العمليات اللاحقة (postfix)
# قم بكتابة دالة تستقبل قيمة نصية من نوع string ، تقوم الدالة
#  باستقبال معادلة رياضية ولكن العمليات الرياضية تكون لاحقة postfix
# ثم تقوم الـ function بحلها وإرجاع النتيجة من نوع integer

def postfix(expr):
    expr_as_list = expr.split()
    x = y = None
    for e in expr_as_list:
        if e.isdigit():
            if x == None :
                x = e
            else :
                y = e
        elif (e == '/' or e == '%') and y == '0' :
            pass
        else :
            x = str(int(eval(x+e+y)))
    return int(x)

print(postfix('2 0 /')) #---> 2
print(postfix('4 2 %')) #---> 0
print(postfix('7 2 ** 40 - 3 /')) #---> 3
print(postfix('4 2 **')) #---> 16
print(postfix('2 3 +'))  # ---> 5
print(postfix('2 3 -'))  # ---> -1
print(postfix('3 3 *')) #---> 9
print(postfix('2 3 * 1 - 5 /')) #---> 1
print(postfix('4 1 - 2 *')) #---> 6
