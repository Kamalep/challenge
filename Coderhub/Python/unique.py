# العثور على العنصر الفريد في المصفوفة
# قم بكتابة دالة تستقبل مصفوفة عدد حقيقي وتقوم هذه الدالة
# بالبحث عن الرقم الفريد في المصفوفة ثم قم بإرجاع النتيجة كمصفوفة من النوع عدد حقيقي

def unique(arr):
    # write your code he
    d = {k: arr.count(k) for k in arr}
    m = min(d.values())
    l = [k for k, v in d.items() if v == m]
    c = arr.count(l[0])
    if l == list(set(arr)) and c > 1:
        return []
    else:
        return l


print(unique([2, 2, 2, 8, 2, 2]))  # --> [8]
print(unique([4, 3, -5, 4]))  # --> [3,-5]
print(unique([1, 2, 1, 2]))  # --> []
print(unique([4, 7, 2, 9, -9]))  # --> [4,7,2,9,-9]
