def partition(customList, l, r):
    i, j = l - 1, l
    while j < r:
        if customList[j] <= customList[r]:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
        j += 1
    i += 1
    customList[r], customList[i] = customList[i], customList[r]
    return i


def quickSort(customList, l, r):
    if l < r:
        i = partition(customList, l, r)
        quickSort(customList, l, i - 1)
        quickSort(customList, i + 1, r)
    return customList


kaka = [23, 4534, 34, 54, 33, 23, 54, 6, 7, 343, 5, 43, 76, 54, 46]
print(quickSort(kaka, 0, len(kaka)-1))
