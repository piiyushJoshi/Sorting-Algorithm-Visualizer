import time

def countingSort(data, drawData, timeTick):
    comparisons = 0  # This won't be used much in counting sort
    swaps = 0

    M = max(data)
    count_array = [0] * (M + 1)

    for num in data:
        count_array[num] += 1

    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(data)

    for i in range(len(data) - 1, -1, -1):
        output_array[count_array[data[i]] - 1] = data[i]
        count_array[data[i]] -= 1
        swaps += 1  
        drawData(output_array, comparisons, swaps)
        time.sleep(timeTick)

    for i in range(len(data)):
        data[i] = output_array[i]
        drawData(data, comparisons, swaps)
        time.sleep(timeTick)
