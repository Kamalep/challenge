def missingletter(txt):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    o = 'No Missing Letter'
    part = abc[abc.index(txt[0]):abc.index(txt[-1]) + 1]
    for c in part:
        if c in txt:
            pass
        else:
            return c
    return o


# def missingletter(txt):
#     abc = 'abcdefghijklmnopqrstuvwxyz'
#     output = 'No Missing Letter'
#     true_chunk = abc[abc.index(txt[0]):abc.index(txt[-1]) + 1]
#     output = [char for char in txt if char not in true_chunk]
#
#     return output

print(missingletter('abcef'))
print(missingletter('mnop'))
print(missingletter('tuvxyz'))
print(missingletter('qrs'))
