def cast_dict(e):
    return {chr: e.count(chr) for chr in e}

def anagrams(word, words):
    return [e for e in words if cast_dict(word) == cast_dict(e)]

w = 'racer'
lst = ['crazer', 'carer', 'racar', 'caers', 'racer']
print(anagrams(w, lst))

w = 'abba'
lst = ['aabb', 'abcd', 'bbaa', 'dada']
print(anagrams(w, lst))

w = 'laser'
lst = ['lazing', 'lazy', 'lacer']
print(anagrams(w, lst))
