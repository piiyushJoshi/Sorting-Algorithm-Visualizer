import time

def insertionSort(data, drawData, timeTick):
    comparisons = 0
    swaps = 0
    n = len(data)
    
    for i in range(1, n):
        key = data[i]
        j = i - 1

        # Compare key with each element on the left until an element smaller than it is found
        while j >= 0 and key < data[j]:
            comparisons += 1  # Increment comparison count
            data[j + 1] = data[j]
            j -= 1
            swaps += 1  # Increment swap count
            drawData(data, comparisons, swaps)
            time.sleep(timeTick)
        
        # Place the key at its correct position
        data[j + 1] = key
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)

        # One final comparison when exiting the while loop
        if j >= 0:
            comparisons += 1
        drawData(data, comparisons, swaps)
