import time

def selectionSort(data, drawData, timeTick):
    comparisons = 0
    swaps = 0
    
    for ind in range(len(data)):
        min_index = ind
        for j in range(ind + 1, len(data)):
            comparisons += 1  # Increment comparison count
            if data[j] < data[min_index]:
                min_index = j
                drawData(data, comparisons, swaps)
                time.sleep(timeTick)

        # Swap only if the minimum index has changed
        if min_index != ind:
            data[ind], data[min_index] = data[min_index], data[ind]
            swaps += 1  # Increment swap count
            drawData(data, comparisons, swaps)
            time.sleep(timeTick)

    drawData(data, comparisons, swaps)  # Final call to drawData
