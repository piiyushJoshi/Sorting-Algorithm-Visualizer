import time

comparisons = 0
swaps = 0

def partition(data, head, tail, drawData, timeTick):
    global comparisons, swaps
    border = head
    pivot = data[tail]
    drawData(data, comparisons, swaps)
    time.sleep(timeTick)
    for j in range(head, tail):
        comparisons += 1
        if data[j] < pivot:
            drawData(data, comparisons, swaps)
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            swaps += 1
            border += 1

    drawData(data, comparisons, swaps)
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    swaps += 1
    return border

def quick_sort(data, head, tail, drawData, timeTick):

    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)
        quick_sort(data, head, partitionIdx - 1, drawData, timeTick)
        quick_sort(data, partitionIdx + 1, tail, drawData, timeTick)

