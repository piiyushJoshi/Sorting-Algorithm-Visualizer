import time

# Initialize global counters for comparisons and swaps
comparisons = 0
swaps = 0

def merge(data, l, m, r, drawData, timeTick):
    global comparisons, swaps

    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = data[l + i]

    for j in range(n2):
        R[j] = data[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        comparisons += 1  # Increment comparison count

        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
        else:
            data[k] = R[j]
            j += 1

        swaps += 1  # Increment swap count
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)
        k += 1

    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1
        swaps += 1  # Increment swap count
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)

    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1
        swaps += 1  # Increment swap count
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)

def mergeSort(data, l, r, drawData, timeTick):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(data, l, m, drawData, timeTick)
        mergeSort(data, m + 1, r, drawData, timeTick)
        merge(data, l, m, r, drawData, timeTick)
