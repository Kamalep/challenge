# خوارزمية Merge Sort
# قم بكتابة function تستقبل مصفوفتين من نوع integer تقوم الـ
# function بدمج المصفوفتين في مصفوفة واحدة مع
# ترتيبها تصاعديا ثم قم بارجاع المصفوفة من نوع integer

# def mergesort(nlist):
#     if len(nlist) > 1:
#         mid = len(nlist) // 2
#         lefthalf = nlist[:mid]
#         righthalf = nlist[mid:]
#         merge_sort(lefthalf)
#         merge_sort(righthalf)
#         i = j = k = 0
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 nlist[k] = lefthalf[i]
#                 i += 1
#             else:
#                 nlist[k] = righthalf[j]
#                 j += 1
#             k += 1
#         while i < len(lefthalf):
#             nlist[k] = lefthalf[i]
#             i += 1
#             k += 1
#
#         while j < len(righthalf):
#             nlist[k] = righthalf[j]
#             j += 1
#             k += 1
#     return nlist
def merge_sort(node1, node2):
    return mergesort(node1 + node2)


def mergesort(nlist):
    if len(nlist) > 1:
        mid = len(nlist) // 2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k] = lefthalf[i]
                i += 1
            else:
                nlist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            nlist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            nlist[k] = righthalf[j]
            j += 1
            k += 1
    return nlist


print(merge_sort([2, 4, 1], [3, 7, 6]))  # ---> [1,2,3,4,6,7]
print(merge_sort([20, 10], [-11, 10]))  # ---> [-11,10,10,20]
print(merge_sort([8, -5], [4]))  # ---> [-5,4,8]
print(merge_sort([1, 2], [3]))  # ---> [1,2,3]
