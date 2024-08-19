import time

comparisons = 0
swaps = 0

def heapify(data, N, i, drawData, timeTick):
    global comparisons, swaps

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Compare with left child
    if l < N:
        comparisons += 1
        if data[largest] < data[l]:
            largest = l

    # Compare with right child
    if r < N:
        comparisons += 1
        if data[largest] < data[r]:
            largest = r

    # Swap if the largest is not the root
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        swaps += 1
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)
        heapify(data, N, largest, drawData, timeTick)

def heapSort(data, drawData, timeTick):
    global comparisons, swaps

    N = len(data)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(data, N, i, drawData, timeTick)

    # Extract elements one by one
    for i in range(N - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        swaps += 1
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)
        heapify(data, i, 0, drawData, timeTick)
