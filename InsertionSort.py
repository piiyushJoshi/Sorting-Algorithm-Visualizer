import time

def insertionSort(data,drawData,timeTick):
    n = len(data)
    if n <= 1:
        return
    for i in range(1, n):
        key = data[i]
        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
            drawData(data)
            time.sleep(timeTick)

        data[j+1] = key 
        drawData(data)
        time.sleep(timeTick)