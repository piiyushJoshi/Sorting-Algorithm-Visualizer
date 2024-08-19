import time
import random

comparisons = 0
swaps = 0

def bogoSort(data, drawData, timeTick):
    global swaps
    global comparisons
    n = len(data)
    
    while not is_sorted(data):
        shuffle(data, drawData, timeTick)
        comparisons += n - 1  # Adding comparisons for each shuffle
        drawData(data, comparisons, swaps)

def is_sorted(data):
    global comparisons
    n = len(data)
    for i in range(0, n - 1):
        comparisons += 1
        if data[i] > data[i + 1]:
            return False
    return True

def shuffle(data, drawData, timeTick):
    global swaps
    n = len(data)
    for i in range(n):
        r = random.randint(0, n - 1)
        data[i], data[r] = data[r], data[i]
        swaps += 1
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)
