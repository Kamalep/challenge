## 2
def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x, y[:-1])
        lcs2 = lcs(x[:-1], y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2


print(lcs("a", "b"))  # => ""
print(lcs("a", "a"))  # =>"a"
print(lcs("abc", "ac"))  # =>"ac"
print(lcs("abcdef", "abc"))  # => "abc")
print(lcs("abcdef", "acf"))  # => "acf")
print(lcs("132535365", "123456789"))  # => "12356")
print(lcs("anothertest", "notatest"))  # => "notatest"
print(lcs("finaltest", "zzzfinallyzzz"))  # => "final"

## 3
# def lcs(x, y):
#     res = []
#     i = 0
#     for item in y:
#         if item in x[i:]:
#             res += [item]
#             i = x.index(item) + 1
#     return "".join(res)


## 4
# def lcs(x, y):
#     n = len(x)
#     m = len(y)
#
#     dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
#
#     for i in range(1, n + 1):
#         for j in range(1, m + 1):
#             if x[i - 1] == y[j - 1]:
#                 dp[i][j] = 1 + dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#
#     l = dp[n][m]
#     if l == 0:
#         return ""
#
#     res = ['$' for i in range(l)]
#     idx = l - 1
#     i, j = n, m
#     while i > 0 and j > 0:
#         if x[i - 1] == y[j - 1]:
#             res[idx] = x[i - 1]
#             idx -= 1
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1
#     return "".join(res)


## 1
# def lcs_h(X, Y, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif X[m - 1] == Y[n - 1]:
#         return 1 + lcs_h(X, Y, m - 1, n - 1)
#     else:
#         return max(lcs_h(X, Y, m, n - 1), lcs_h(X, Y, m - 1, n))
#
#
# X = "AGGTAB"
# Y = "GXTXAYB"
# print("Length of LCS is ", lcs_h(X, Y, len(X), len(Y)))
