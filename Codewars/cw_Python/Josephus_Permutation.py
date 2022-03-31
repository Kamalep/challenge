# with while loop
def josephus(items, k):
    heroes = []
    k -= 1
    idx = 0
    while len(items) > 0:
        idx = (idx + k) % len(items)
        heroes.append(items.pop(idx))
    return heroes

# with recursion
def josephus1(items, k, idx=0, heroes=[]):
    if not items:
        return items
    elif len(items) == 1:
        heroes.append(items.pop())
        return heroes
    else:
        idx = (idx + (k - 1)) % len(items)
        heroes.append(items.pop(idx))
        return josephus(items, k, idx, heroes)


print(josephus([10, 20, 30], 2))  # --> 20 10 30 ok
print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))  # ---> [1,2,3,4,5,6,7,8,9,10]
print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))  # ---> [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
print(josephus(["C", "o", "d", "e", "W", "a", "r", "s"], 4))  # ---> ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'] ok
print(josephus([1, 2, 3, 4, 5, 6, 7], 3))  # ---> [3, 6, 2, 7, 5, 1, 4]
print(josephus([], 3))  # ---> [] ok
print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
               40))  # ---> [10, 7, 8, 13, 5, 4, 12, 11, 3, 15, 14, 9, 1, 6, 2]
