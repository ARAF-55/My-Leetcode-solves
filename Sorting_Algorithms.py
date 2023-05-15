import math


def bubbleSort(customList):
    for i in range(len(customList) - 2):
        for j in range(len(customList) - 1 - i):
            if customList[j] > customList[j + 1]:
                temp = customList[j]
                customList[j] = customList[j + 1]
                customList[j + 1] = temp
    return customList


def selectionSort(customList):
    for i in range(len(customList) - 1):
        min_value_idx = i
        for j in range(i + 1, len(customList)):
            if customList[j] < customList[min_value_idx]:
                min_value_idx = j
        temp = customList[i]
        customList[i] = customList[min_value_idx]
        customList[min_value_idx] = temp
    return customList


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


def bucketSort(customList):
    num_of_buckets = round(math.sqrt(len(customList)))
    arr = []
    for i in range(num_of_buckets):
        arr.append([])
    maxValue = max(customList)
    for j in customList:
        idx = math.ceil(j * num_of_buckets / maxValue)
        arr[idx - 1].append(j)
    for i in range(len(arr)):
        arr[i] = insertionSort(arr[i])
    k = 0
    for i in range(num_of_buckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = customList[l + i]
    for i in range(n2):
        R[i] = customList[m + 1 + i]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] < R[j]:
            customList[k] = L[i]
            i += 1
            k += 1
        else:
            customList[k] = R[j]
            j += 1
            k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList, l, r):
    if l < r:
        m = (l + r + 1) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList


def partition(customList, low, high):
    pivot = customList[high]
    i = low - 1
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            temp = customList[i]
            customList[i] = customList[j]
            customList[j] = temp
    i += 1
    temp = customList[high]
    customList[high] = customList[i]
    customList[i] = temp
    return i


def quickSort(customList, low, high):
    if low < high:
        idx = partition(customList, low, high)
        quickSort(customList, low, idx - 1)
        quickSort(customList, idx + 1, high)
    return customList


def heapify(customList, n, i):
    largest = i
    left_idx = 2 * i + 1
    right_idx = 2 * i + 2
    if left_idx < n and customList[largest] < customList[left_idx]:
        largest = left_idx
    if right_idx < n and customList[largest] < customList[right_idx]:
        largest = right_idx
    if largest != i:
        customList[i], customList[largest] = customList[largest], customList[i]
        heapify(customList, n, largest)


def heapSort(customList):
    for i in range(len(customList)-1, -1, -1):
        heapify(customList, len(customList), i)
    for i in range(len(customList) - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    return customList


# jaka = [53, 67, 33, 88, 99, 12, 34, 65, 43]
# kaka = [23, 6, 34, 8, 64, 99, 45, 67, 44, 99, 23, 467, 85, 90, 9, 56]
kaka = [23, 6, 34]

kaka = mergeSort(kaka, 0, len(kaka)-1)

print(kaka)
