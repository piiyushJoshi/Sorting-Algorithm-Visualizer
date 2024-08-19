import time

def bubble_sort(data, drawData, timeTick):
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    for _ in range(len(data) - 1):
        for j in range(len(data) - 1):
            comparisons += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
                drawData(data, comparisons, swaps)
                time.sleep(timeTick)
    drawData(data, comparisons, swaps)
